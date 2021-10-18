from django import forms

from .models import coordinateInfo


class UpLoadCoordinateForm(forms.ModelForm):
    """服情報登録フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = coordinateInfo
        fields = ('coordinate_name', 'image',)
