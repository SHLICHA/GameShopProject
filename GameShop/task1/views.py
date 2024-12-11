from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


from .forms import UserRegister
from .models import *


class Platform(TemplateView):
    template_name = "platform.html"


def games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games.html', context=context, )


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь с таким именем уже существует'
            else:
                Buyer.objects.create(
                    name=username,
                    age=age)
                return HttpResponse(f'Приветствуем, {username}')
    else:
        info['form'] = UserRegister()
    return render(request, 'registration_page.html', context=info)


def news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': page_obj
    }
    return render(request, 'news.html', context)