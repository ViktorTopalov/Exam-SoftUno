from django import forms

from final_exam_project.profile.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }
        labels = {
            'password': 'Password',
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']
        password = forms.CharField(widget=forms.PasswordInput, required=False)


class DeleteProfileForm(forms.Form):
    pass
