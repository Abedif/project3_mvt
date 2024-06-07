from django.shortcuts import render

def agents_grid(request):
    return render(request , 'agents/agents-grid.html')

# Create your views here.
