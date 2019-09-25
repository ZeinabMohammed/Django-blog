from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	content = forms.CharField(
        label = 'Add Comment',
        max_length = 1000,
        required = True,
        widget = forms.TextInput(
            attrs = {'class': 'summernote', 'name': 'comment'}
        )
    )
	class Meta:
		model = Comment
		fields = [ 'content']

		def __str__(self):
			return self.user