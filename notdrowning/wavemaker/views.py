from django.shortcuts import render

from .forms import WaveForm


def index(request):

    if request.method == 'POST':
        form = WaveForm(request.POST)
        if form.is_valid():
            ripple = form.save()
            print(ripple.frequency)
    else:
        initial_dict = {
            'shape': 'SQU',
            'frequency': 400,
            'bitrate': 40000
        }

        form = WaveForm(initial=initial_dict)

    return render(request, 'wavemaker/index.html', {'form': form})
