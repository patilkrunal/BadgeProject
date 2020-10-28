from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse

from .models import StudentMembership


def get_student_membership(request):
    student_membership_qs = StudentMembership.objects.filter(user=request.user)
    if student_membership_qs.exists():
        return student_membership_qs.first()
    return None


def get_selected_membership(request):
    student_membership_type =  request.session['selected_student_membership_type']
    selected_student_membership_qs = StudentMembership.objects.filter(membership_type=student_membership_type)
    if selected_student_membership_qs.exists():
        return selected_student_membership_qs.first()
    return None


class MembershipSelectView(ListView):
    template_name = 'memberships/membership_list.html'
    context_object_name = 'memberships'
    model = StudentMembership

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_student_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self,request,*args,**kwargs):
        selected_membership_type = request.POST.get('membership_type')

        user_membership = get_student_membership(self.request)

        selected_membership_qs = StudentMembership.objects.filter(membership_type=selected_membership_type)
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()

        request.session['selected_membership_type'] = selected_membership.membership_type
        
        return HttpResponseRedirect(reverse('memberships:payment'))