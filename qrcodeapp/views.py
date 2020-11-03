from django.shortcuts import render
from .models import QRcodeModel

from memberships.badge_generator import generate_badge

def badge_generator_view(request):
    
    context = {
        'img_url': generate_badge(request)
    }

    return render(request, 'qrcodeapp/badge_wIth_QRcode.html', context)