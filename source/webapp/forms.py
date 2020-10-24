from django import forms
from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'signature']
        widgets = {'signature': forms.Textarea(attrs={'class': 'form-signature'})}

