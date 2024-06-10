from django.shortcuts import render
from .models import Service,Testimonial
from property.models import Property
from agents.models import Agents
from blogs.models import New

def home(request):

    context = {
        'services' : Service.objects.filter(status=True),
        'properties' : Property.objects.filter(status=True),
        'agents' : Agents.objects.filter(status=True),
        'news' : New.objects.filter(status=True),
        'testimonials' : Testimonial.objects.filter(status=True),
    }

    return render(request ,'root/index.html' , context=context)

def about(request):

    context ={
        'agents' : Agents.objects.filter(status=True)
    }

    return render(request ,'root/about.html' ,context=context)


def contact(request):
    return render(request , 'root/contact.html' )


# Create your views here.
