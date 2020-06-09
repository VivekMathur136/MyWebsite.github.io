from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("this is my homepage (/)")
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is my about page (/about)")


def projects(request):
    return render(request, 'projects.html')
    # return HttpResponse("this is my projects page (/projects)")
