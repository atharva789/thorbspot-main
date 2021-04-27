from django import forms 

from .models import Blog

class BlogPostForm(forms.Form):
  title       = forms.CharField(
    widget = forms.Textarea(
      attrs={
        "placeholder":"Title",
        "rows":5,
        "class":"col"
      }
    )
  )
  description = forms.CharField(
    widget = forms.Textarea(
      attrs={
        "placeholder":"Description",
        "rows":5,
        "class":"col"
      }
    )
  )
  blog        = forms.CharField(
    widget = forms.Textarea(
      attrs = {
        "placeholder":"Blog",
        "rows":10,
        "class":"col"
      }
    )
  )
  smm         = forms.BooleanField(
    required = False,
    widget = forms.CheckboxInput(
      attrs = {
        "class":"col"
      }
    )
  )