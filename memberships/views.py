from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

from .models import StudentMembership
from courses.models import Course
from . import forms


class StudentsListView(generic.ListView):
    model = StudentMembership
    template_name = 'memberships/membership_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        student_membership_qs = StudentMembership.objects.all()
        list = [l for l in [s for s in student_membership_qs]]
        context= {'student_membership_qs': list}
        return context

    @login_required
    def add_members(request):
      if request.method == 'POST':
        form = forms.AddMembers(request.POST, request.FILES)
        if form.is_valid():
          instance = form.save(commit=False)
          instance.author = request.user
          instance.save()
          return redirect('courses:course_list')
      else:
        form = forms.AddMembers()
      return render(request, 'memberships/add_members.html', { 'form': form })


# class CourseDetailRedirect(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         try:
#           pk = self.args.get('pk')
#         except:
#           pk=1
        
#         try:
#           course = Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#           course = Course.objects.get(pk=1)
        
#         return reverse('courses:course_detail', course.slug)