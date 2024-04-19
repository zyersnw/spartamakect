from django import forms
from .models import Item , Comment


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'image']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.user = kwargs.pop('user', None)

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        if self.user:
            comment.author = self.user
        if commit:
            comment.save()
        return comment