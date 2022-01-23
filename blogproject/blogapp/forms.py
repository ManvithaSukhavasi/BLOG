from django import forms
from blogapp.models import Blogs

class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        exclude=['likes','date']