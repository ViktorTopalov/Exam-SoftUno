from django.urls import path

from final_exam_project.home.views import index

urlpatterns = (
    path('',index,name='index'),
)