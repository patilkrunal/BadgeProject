from django.views import generic

from .models import StudentMembership


class StudentsListView(generic.ListView):
    model = StudentMembership
    template_name = 'memberships/membership_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        student_membership_qs = StudentMembership.objects.all()
        list = [l for l in [s for s in student_membership_qs]]
        context= {'student_membership_qs': list}
        return context