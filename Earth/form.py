from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
                    "relate",
                    "caption",
                    "description",
                    "image",
                    "profile_pic"
            ]
            
            
        