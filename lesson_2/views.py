from django.shortcuts import render


def index(request):
    return render(request, 'start.html')


def bio(request, username):
    print(username)
    return render(request, 'index.html')

