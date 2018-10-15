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
    }
]

boilerPlate = [
    {
        'start': 'def main(): \n',
        'end': 'if __name__ == \"__main__\":\n main() \n'
    }
]

consoleMessage = [
    {
        'message': 'Hello World!'
    }
]

def index(request):
    context = {
        'apiKey': apiKey,
        'boilerPlate': boilerPlate,
        'consoleMessage': consoleMessage,
        'title': 'Level 1'
    }
    return render(request, 'home/index.html', context)