_author_ = 'ivan'

from django.forms import ModelForm
from lesson.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']


