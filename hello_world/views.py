from django.shortcuts import render


def hello_world(request):
    # Test of the debugger
    youngblod = "Hola"
    return render(request, 'hello_world.html', {})
