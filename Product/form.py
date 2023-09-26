from django import forms

from .models import Reviews
class FormReviews(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=['Name','Email','Review']