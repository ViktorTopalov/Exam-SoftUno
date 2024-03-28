from django.shortcuts import redirect, render

from final_exam_project.profile.forms import ProfileCreateForm, ProfileEditForm, DeleteProfileForm
from final_exam_project.profile.models import Profile


def get_profile():
    return Profile.objects.first()

def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return redirect('index')
    else:
        form = ProfileCreateForm()

    return render(request, 'profiles/profile-create.html', {'form': form})


def profile_details(request):
    user_profile = Profile.objects.first()


    return render(request, 'profiles/profile-details.html', {'user_profile': user_profile})

def edit_profile(request):
    user_profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'profiles/profile-edit.html', {'form': form})

def delete_profile(request):
    user_profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST)
        if form.is_valid():

            user_profile.delete()
            return redirect('index')
    else:
        form = DeleteProfileForm()

    return render(request, 'profiles/profile-delete.html', {'form': form})