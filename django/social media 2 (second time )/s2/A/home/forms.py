from django import forms
from .models import Post , Comment

class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)



class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = { #widgets are different in model forms in comparison with forms
            'body': forms.Textarea(attrs={'class':'form_control'}),
        #   ^-> field : widngets
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('body',)

class PostSearchForm(forms.Form):
    search  = forms.CharField()