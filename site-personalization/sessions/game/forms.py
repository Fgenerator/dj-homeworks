from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.TextInput, label=False)

    class Meta(object):
        model = Game
        exclude = ('id', 'is_finished', 'players', 'final_attempts')