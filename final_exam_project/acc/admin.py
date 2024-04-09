from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from final_exam_project.acc.forms import ProjectUserChangeForm, ProjectUserCreation

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class ProjectUserAdmin(UserAdmin):
    model = UserModel
    add_form = ProjectUserCreation
    form = ProjectUserChangeForm
    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email', 'is_superuser')
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )
    add_fieldsets = (
        (
            None,{"classes": ("wide",),
                  "fields":("email", "password1", "password2","is_staff", "is_superuser", "user_permissions",),
                  }
        ),)
