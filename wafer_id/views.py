from django.shortcuts import render
from .models import Box

class WebPages:
    HOME_PAGE = "website/home.html"
    BOX = "website/box.html"
    BOXES = "website/boxes.html"
    LOGIN_USER = "website/login-user.html"
    PRIVACY_POLICY = "website/privacy-policy.html"
# Create your views here.

def home(request):
    return render(request, WebPages.HOME_PAGE)

def boxes(request):
    boxes = Box.objects.all()
    return render(request, WebPages.BOXES, {'boxes': boxes})

