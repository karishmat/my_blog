from django import forms
from .models import SignUp,Comment,Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields={'title','body','user','email'}

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields='__all__'
        # fields={'first_name','last_name'}   ------allows us display only fname and lname on form

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields={'comment','commenter','email'}