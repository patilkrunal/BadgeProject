from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms

from memberships.models import StudentMembership
from .models import Course, Branch_of_study
from courses.forms import CreateCourse, CreateBranch


class CourseListView(ListView):
    context_object_name = 'courses'
    template_name = 'courses/course_list.html'
<<<<<<< HEAD
      
=======
    model = Course
>>>>>>> a66239a5d7340750dc190f3c577810f98e78fe6e

    @login_required
    def course_create(request):
        if request.method == 'POST':
            form = CreateCourse(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                form.instance.creator = request.user
                instance.save()
                return redirect('courses:course_list')
        else:
            form = CreateCourse()
        return render(request, 'courses/course_create.html', {'form': form})


class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    queryset = Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['student_membership'] = StudentMembership.objects.all()
        context['courses'] = Course.objects.all()
        context['branches'] = Branch_of_study.objects.all()
        
        return context


    @login_required
    def branch_create(request):
        if request.method == 'POST':
            form = CreateBranch(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('courses:course_create')
        else:
            form = CreateBranch()
        return render(request, 'courses/branch_create.html', {'form': form})
