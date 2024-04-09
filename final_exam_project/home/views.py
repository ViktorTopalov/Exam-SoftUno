from django.contrib.auth import get_user_model
from django.shortcuts import render

from final_exam_project.profile.models import Profile

# Create your views here.


def index(request):
        return render(request, 'home/index.html')

