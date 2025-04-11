from django import forms
from .models import Post

class PostCreateForm(form.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'image', 'location', 'category']
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }