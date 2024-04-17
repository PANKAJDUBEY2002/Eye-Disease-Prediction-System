from django import forms

class EyeImageForm(forms.Form):
    eye_image = forms.ImageField()
