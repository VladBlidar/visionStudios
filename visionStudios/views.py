from django.shortcuts import render

def homePage(request):
    if request.method == 'GET':
        return render(request, "home.html")

def modelsPage(request):
    if request.method == 'GET':
        return render(request, "models.html")

def aboutUsPage(request):
    if request.method == 'GET':
        return render(request, "aboutUs.html")

def galeryPage(request):
    if request.method == 'GET':
        return render(request, "galery.html")
