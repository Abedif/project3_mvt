from django.shortcuts import render


def home(request):
    return render(request ,'root/index.html')

def about(request):
    return render(request ,'root/about.html')


def contact(request):
    return render(request , 'root/contact.html')

def blogs (request):
    return render(request , 'blogs/blog-grid.html')

def property_grid(request):
    return render(request , 'property/property-grid.html')

def agents_grid(request):
    return render(request , 'agents/agents-grid.html')

# Create your views here.
