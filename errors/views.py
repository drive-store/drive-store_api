from django.shortcuts import render

def get404error(request, exception):
    return render(request, '404.html', {}, status=404)

def get500error(request, exception):
    return render(request, '500.html', {}, status=500)
