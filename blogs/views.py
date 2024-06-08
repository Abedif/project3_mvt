from django.shortcuts import render

def blogs (request):
    return render(request , 'blogs/blog-single.html')


# Create your views here.
