from django.shortcuts import render


def index(request):
    return render(request, 'wavemaker/index.html')
