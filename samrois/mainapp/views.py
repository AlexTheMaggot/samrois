# ExternalImports
import telebot
# End ExternalImports

# DjangoImports
from django.shortcuts import render, redirect, get_object_or_404
# End DjangoImports

# InternalImports
from .models import Slide, Tour, Order
# End InternalImports

# BotApi
bot = telebot.TeleBot('1658154978:AAGnajG-o5cDpCvWU53qyJXKkopnQgTpzfc')
# End BotApi


# 404Handler
def custom_404(request, exception):
    if '/en/' in request.path:
        template = 'mainapp/en/404.html'
    elif '/ko/' in request.path:
        template = 'mainapp/ko/404.html'
    elif '/uz/' in request.path:
        template = 'mainapp/uz/404.html'
    else:
        template = 'mainapp/ru/404.html'
    return render(request, template)
# End 404Handler


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
    elif '/uz/' in request.path:
        template = 'mainapp/uz/index.html'
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
    elif '/uz/' in request.path:
        template = 'mainapp/uz/tour_list.html'
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
    elif '/uz/' in request.path:
        template = 'mainapp/uz/tour_detail.html'
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
        if 'tour' in request.POST:
            tour = Tour.objects.get(id=request.POST['tour'])
            order = Order(name=name, phone=phone, email=email, comment=comment, tour=tour)
        else:
            order = Order(name=name, phone=phone, email=email, comment=comment, tour=None)
        order.save()

        message = 'Новая заявка!\r\n\r\nИмя:\r\n' + name + '\r\n\r\nНомер телефона:\r\n' + phone
        message += '\r\n\r\nE-mail:\r\n' + email

        if 'tour' in request.POST:
            tour_object = Tour.objects.get(id=request.POST['tour'])
            tour = tour_object.name_ru
            message += '\r\n\r\nНаправление:\r\n' + tour
        if comment != '':
            message += '\r\n\r\nКомментарий:\r\n' + comment

        bot.send_message(-1001163956964, message)

        if '/en/' in request.path:
            url = 'en_thank_you'
        elif '/ko/' in request.path:
            url = 'ko_thank_you'
        elif '/uz/' in request.path:
            url = 'uz_thank_you'
        else:
            url = 'ru_thank_you'

        return redirect(url)
# End OrderCreate


# ThankYou
def thank_you(request):
    if '/en/' in request.path:
        template = 'mainapp/en/thank-you.html'
    elif '/ko/' in request.path:
        template = 'mainapp/ko/thank-you.html'
    elif '/uz/' in request.path:
        template = 'mainapp/uz/thank-you.html'
    else:
        template = 'mainapp/ru/thank-you.html'
    return render(request, template)

# End ThankYou
