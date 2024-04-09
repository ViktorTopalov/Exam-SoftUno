from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from final_exam_project.profile.forms import ProfileEditForm, DeleteProfileForm
from final_exam_project.profile.models import Profile


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"
    form_class = ProfileEditForm


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-edit.html"
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse("profile_details", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user.profile


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-delete.html"
    form_class = DeleteProfileForm
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect('index')


UserModel = get_user_model()






