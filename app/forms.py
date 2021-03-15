from django.forms import ModelForm
from django import forms
from app.models import Status

class StatusModelForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['author', 'content', 'image']

    # validate content length
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')

        if len(content) > 240:
            raise forms.ValidationError("Content is too long.")
        
        return content

    # validate content or image upload
    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content', None)
        if content == "":
            content = None

        image = self.cleaned_data.get('image', None)

        if content is None and image is None:
            raise forms.ValidationError("Content or Image is required")
        
        return super().clean(*args, **kwargs)

    
        
