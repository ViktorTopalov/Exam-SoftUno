from django.shortcuts import render

from final_exam_project.profile.models import Profile


# Create your views here.

def get_profile():
    return Profile.objects.first()

def index(request):
    if get_profile():
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/home_without_profile.html')
