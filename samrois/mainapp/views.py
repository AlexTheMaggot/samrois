# DjangoImports
from django.shortcuts import render, redirect, get_object_or_404
from .models import Slide, Tour, Order
# End DjangoImports


# RedirectToIndexPage
def redirect_to_index(request):
    return redirect('ru_index')
# End RedirectToIndexPage


# IndexView
def index(request):
    tours = Tour.objects.all()
    slides = Slide.objects.all()
    context = {
        'slides': slides,
        'tours': tours,
    }
    # CheckLanguage
    if '/en/' in request.path:
        template = 'mainapp/en/index.html'
    elif '/ko/' in request.path:
        template = 'mainapp/ko/index.html'
    else:
        template = 'mainapp/ru/index.html'
    # End CheckLanguage
    return render(request, template, context)
# End IndexView


# TourListView
def tour_list(request):
    tours = Tour.objects.all()
    context = {
        'tours': tours,
    }
    # CheckLanguage
    if '/en/' in request.path:
        template = 'mainapp/en/tour_list.html'
    elif '/ko/' in request.path:
        template = 'mainapp/ko/tour_list.html'
    else:
        template = 'mainapp/ru/tour_list.html'
    # End CheckLanguage
    return render(request, template, context)
# End TourListView


# TourDetailView
def tour_detail(request, tour_id):
    tours = Tour.objects.exclude(id=tour_id)
    tour = get_object_or_404(Tour, id=tour_id)
    context = {
        'tours': tours,
        'tour': tour,
    }
    # CheckLanguage
    if '/en/' in request.path:
        template = 'mainapp/en/tour_detail.html'
    elif '/ko/' in request.path:
        template = 'mainapp/ko/tour_detail.html'
    else:
        template = 'mainapp/ru/tour_detail.html'
    # End CheckLanguage
    return render(request, template, context)
# End TourDetailView


# OrderCreate
def order_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        comment = request.POST['comment']

        order = Order(name=name, phone=phone, email=email, comment=comment)
        order.save()
        return redirect('ru_index')
# End OrderCreate
