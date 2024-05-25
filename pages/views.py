from django.shortcuts import render


def index(request):
    return render(request, 'pages/templates/base.html')