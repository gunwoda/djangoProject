from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'v2/index.html')
def name(request):
    return render(request, 'v2/name.html')
