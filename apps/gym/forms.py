from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from apps.users.models import User

from .models import Attendee, Gym


class GymForm(forms.Form):
    """Simple form for Gym model."""
    name = forms.CharField()
    boss = forms.ModelChoiceField(
        User.objects.all(),
    )
    description = forms.CharField(
        widget=forms.Textarea(),
        required=False,
    )

    def clean_name(self):
        name = self.cleaned_data['name']

        if Gym.objects.filter(name=name):
            raise forms.ValidationError(
                "This name already exists.",
            )

        return name


class AttendeeModelForm(forms.ModelForm):
    """Model form for attendee model."""
    class Meta:
        model = Attendee
        fields = (
            'user',
            'gym',
            'subscription',
        )
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': 'This user already have subscription here',
            },
        }
        labels = {
            'gym': 'Name of gym',
        }
        help_texts = {
            'subscription': 'Choose subscription to become attendee',
        }
        # widgets = {
        #     'subscription': forms.TextInput(),
        # }
