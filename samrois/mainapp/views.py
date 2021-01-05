# DjangoImports

from django.shortcuts import render, redirect

# End DjangoImports


# RedirectToIndexPage

def redirect_to_index(request):
    return redirect('ru_index')

# End RedirectToIndexPage


# IndexView

def index(request):
    template = 'mainapp/index.html'
    return render(request, template)

# End IndexView
