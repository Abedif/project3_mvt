from django.shortcuts import render
from .models import Category_Property , Property
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage


def property_grid(request , **kwargs):

    if kwargs.get('category_pro'):
        
        all_service = Property.filter(category_pro__title = kwargs.get('category_pro'))

    else:
        all_service = Property.objects.filter(status=True)


    all_services = Paginator(all_service , 3)
    last_page = all_services.num_pages

    try:
        page_number = request.GET.get('page')
        all_services = all_services.get_page(page_number)

    except PageNotAnInteger:
        all_services = all_services.get_page(1)

    except EmptyPage:
        all_services = all_services.get_page(1)
    
    context ={
        'category_pro' : Category_Property.objects.all() ,
        'property' : all_services , 
        'last_page' : last_page ,
    }

    return render(request , 'property/property-grid.html' , context=context)



def property_single(request , id):

    single = Category_Property.objects.get(id = id)

    context = {
        'detail' : single ,
    }

    return render(request , 'property/property-single.html' , context=context)


# Create your views here.
