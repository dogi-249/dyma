from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import coordinateInfo



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