from django import forms 

from .models import Blog

class BlogPostForm(forms.Form):
  title       = forms.CharField()
  description = forms.CharField()
  blog        = forms.CharField(
    widget = forms.Textarea(
      attrs={
        "placeholder":"Blog",
        "rows":20
      }
    )
  )
  smm         = forms.BooleanField(
    required = False
  )