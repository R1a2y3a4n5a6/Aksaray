from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='restaurant/index.html')

def menu(request):
    return render(request, template_name='restaurant/menu.html')