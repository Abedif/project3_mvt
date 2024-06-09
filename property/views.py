from django.shortcuts import render
from .models import Category_Property , Property
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage


def property_grid(request):
    
    context ={
        'category_pro' : Category_Property.objects.filter(status = True) ,
        'property' : Property.objects.filter(status = True)
    }

    return render(request , 'property/property-grid.html' , context=context)



def property_single(request):
    return render(request , 'property/property-single.html')


# Create your views here.
