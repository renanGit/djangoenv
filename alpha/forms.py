from .models import AlphaBoard
from django.forms import Textarea, ModelForm


class AlphaBoardForm(ModelForm):
    class Meta:
        model = AlphaBoard
        fields = ('title', 'alpha_text',)
        exclude = ('created_on', 'modified_on',)
        widgets = {
            'alpha_text': Textarea(attrs={'rows': 4, 'cols': 40}),
        }
