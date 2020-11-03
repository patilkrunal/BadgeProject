from django.views.generic import TemplateView
from courses.models import Course

class HomePageView(TemplateView):
    context_object_name = 'courses'
    template_name = 'home/index.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        
        return context
