from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect

from memberships.models import StudentMembership
#,Subscription
from .forms import profileUpdateForm,tutorUpdateForm
from .models import Profile


def get_tutor_membership(request):
    tutor_membership_qs = StudentMembership.objects.filter(tutor=request.tutor)
    if tutor_membership_qs.exists():
        return tutor_membership_qs.first()
    return None

""" def get_tutor_subscription(request):
    tutor_subscription_qs = Subscription.objects.filter(tutor_membership = get_tutor_membership(request))
    if tutor_subscription_qs.exists():
        tutor_subscription = tutor_subscription_qs.first()
        return tutor_subscription
    return None """


@login_required
def Profile(request):
    tutor_membership = get_tutor_membership(request)
    #tutor_subscription = get_tutor_subscription(request)
    
    if request.method== 'POST':
        u_form = tutorUpdateForm(request.POST,instance=request.tutor)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.tutor.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated!')
            return redirect('tutors:profile')
    else:
        u_form = tutorUpdateForm(instance=request.tutor)
        p_form = profileUpdateForm(instance=request.tutor.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
        'tutor_membership':tutor_membership
        #'tutor_subscription': tutor_subscription
    }
    return render(request,'profile/profile.html',context)
