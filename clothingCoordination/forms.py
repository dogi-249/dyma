from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import coordinateInfo
from accounts.models import User


class UpLoadCoordinateForm(forms.ModelForm):
    """服情報登録フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = coordinateInfo
        fields = ('coordinate_name', 'image',)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'u-border-1 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-custom-font u-input u-input-rectangle u-text-font'
            self.fields['username'].widget.attrs['id'] = 'name-f2a8'

    class Meta:
        model = User
        fields = ('username', 'email', 'years', 'sex', 'body_height', 'email', 'password1', 'password2')
        widgets = {
            'username': ()
        }

