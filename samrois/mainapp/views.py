# DjangoImports

from django.shortcuts import render, redirect

# End DjangoImports


# RedirectToIndexPage

def redirect_to_index(request):
    return redirect('ru_index')

# End RedirectToIndexPage


# IndexView

def index(request):

    # CheckLanguage
    if '/ru/' in request.path:
        template = 'mainapp/ru/index.html'
    elif '/en/' in request.path:
        template = 'mainapp/en/index.html'
    elif '/kr/' in request.path:
        template = 'mainapp/kr/index.html'
    else:
        template = 'mainapp/ru/index.html'
    # End CheckLanguage

    return render(request, template)

# End IndexView
