from django.forms import ModelForm
from wavemaker.models import Wave


class WaveForm(ModelForm):
    """
    A Django form used to create a model. No way this could get confusing.
    """
    class Meta:
        model = Wave
        fields = ['shape', 'frequency', 'bitrate']
