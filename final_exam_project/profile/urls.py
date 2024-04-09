

from django.urls import path, include

from final_exam_project.profile.views import ProfileDetailsView, \
    ProfileUpdateView, DeleteProfileView

urlpatterns = (
        path('<int:pk>/', ProfileDetailsView.as_view(), name='profile_details'),
        path('<int:pk>/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
        path('<int:pk>/delete/', DeleteProfileView.as_view(), name='delete_profile'),
         )
