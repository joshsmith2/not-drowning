from django.shortcuts import render
from django.http import HttpResponseRedirect
from wavemaker.models import Wave

from .forms import WaveForm


def index(request):

    if request.method == 'POST':
        form = WaveForm(request.POST)
        if form.is_valid():
            ripple = form.save()
            print(ripple.frequency)
    else:
        form = WaveForm()

    return render(request, 'wavemaker/index.html', {'form': form})
