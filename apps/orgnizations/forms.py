from django import forms
from apps.operations.models import UserAsk


class AskAddForm(forms.ModelForm):

    class Meta:
        model=UserAsk
        fields=['name','mobile','course_name']
