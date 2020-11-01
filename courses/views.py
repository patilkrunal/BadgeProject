from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import TemplateView,ListView,DetailView,View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms

from .models import Course, Branch_of_study
from memberships.models import StudentMembership
from . import forms


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category = Branch_of_study.objects.all()
        context['category'] = category
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class CourseListView(ListView):
    context_object_name = 'courses'
    template_name = 'courses/course_list.html'
    model = Course

    @login_required
    def course_create(self, request):
        if request.method == 'POST':
            form = forms.CreateCourse(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('courses:course_list')
        else:
            form = forms.CreateCourse()
        return render(request, 'courses/course_create.html', { 'form': form })


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
