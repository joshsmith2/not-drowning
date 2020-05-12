from django.db import models


class Wave(models.Model):
    # TODO: Sensible maxes and mins: 20 to 2K
    frequency = models.DecimalField(max_digits=5, decimal_places=3)
    bitrate = models.PositiveIntegerField()

    SINE = "SIN"
    SQUARE = "SQU"
    TRIANGLE = "TRI"
    WAVE_CHOICES = [
        (SINE, 'Sine'),
        (SQUARE, 'Square'),
        (TRIANGLE, 'Triangle'),
    ]
    shape = models.CharField(
        max_length=3,
        choices=WAVE_CHOICES,
        default=SINE
    )


    # Other model logic - see https://www.digitalocean.com/community/tutorials/how-to-create-django-models
    class Meta:
        ordering = ['frequency','shape', 'bitrate']
