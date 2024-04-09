from django.urls import path

from final_exam_project.acc.views import LoginUserView, RegisterUserView, ProjectUserLogOut

urlpatterns=(
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("logout/",ProjectUserLogOut.as_view(),name="logout_user" )
)