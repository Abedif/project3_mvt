from django.shortcuts import render
from .models import Agents
from property.models import Property , Category_Property


def agents_grid(request):

    agent = Agents.objects.filter(status=True)

    context={
        'agents' : agent 
    }

    return render(request , 'agents/agents-grid.html' , context=context)



def agent_single(request , id):

    agent = Agents.objects.get(id=id)

    context={
        'agent' : agent ,
        'property' : Property.objects.filter(status=True) ,
        'category' : Category_Property.objects.filter(status=True)
    }

    return render(request , 'agents/agent-single.html' , context=context)




# Create your views here.
