from django.contrib.auth import views as auth_views, login, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views

from final_exam_project.acc.forms import ProjectUserCreation, ProjectUserLoginForm
from final_exam_project.profile.models import Profile

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    form_class = ProjectUserLoginForm
    template_name = 'acc/login.html'

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class RegisterUserView(views.CreateView):
    model = UserModel
    form_class = ProjectUserCreation
    template_name = 'acc/register.html'
    success_url = reverse_lazy("login_user")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


class ProjectUserLogOut(auth_views.LogoutView):
    success_url = reverse_lazy("index")
