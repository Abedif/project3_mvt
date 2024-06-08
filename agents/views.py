from django.shortcuts import render

def agents_grid(request):
    return render(request , 'agents/agents-grid.html')

def agent_single(request):
    return render(request , 'agent/agent-single.html')

# Create your views here.
