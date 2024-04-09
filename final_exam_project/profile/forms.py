from django import forms

from final_exam_project.profile.models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'profile_picture']
        password = forms.CharField(widget=forms.PasswordInput, required=False)


class DeleteProfileForm(forms.Form):
    pass
