from django.forms import ModelForm

from .models import EventObj, SubEventObj


class CreateEvent(ModelForm):
    class Meta:
        model = EventObj
        fields = ['title', 'descripations', 'is_public']


class CreateSubEvent(ModelForm):
    class Meta:
        model = SubEventObj
        fields = ['title', 'descripations', 'guest_user', 'is_offline']
