from django.shortcuts import render


def start_view(request):
    context = {}
    return render(request, 'webpage/index.html', context)


def imprint_view(request):
    context = {}
    return render(request, 'webpage/imprint.html', context)


def about_view(request):
    context = {}
    return render(request, 'webpage/about.html', context)
