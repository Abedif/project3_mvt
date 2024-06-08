from django.shortcuts import render


def blog(request):
    return render(request , 'blogs/blog-grid.html')

def blog_detail (request):
    return render(request , 'blogs/blog-single.html')


# Create your views here.
