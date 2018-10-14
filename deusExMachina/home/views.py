from django.shortcuts import render
from django.http import HttpResponse

# Mock data
apiKey = [
    {
        'method': 'moveLeft()',
        'description': 'Moves robot to the left',
        'example': 'example'
    },
    {
        'method': 'moveRight()',
        'description': 'Moves robot to the right',
        'example': 'example'
    },
    {
        'method': 'moveForward()',
        'description': 'Moves robot to the forward',
        'example': 'example'
    },
    {
        'method': 'moveBack()',
        'description': 'Moves robot to the back',
        'example': 'example'
    },
]

def index(request):
    context = {
        'apiKey': apiKey,
        'title': ''
    }
    return render(request, 'home/index.html', context)