from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'home/index.html')
    # return HttpResponse("""
    #     <h1>Title</h1>
    #     Hello world!!!!!
    #     <input/ type='text'>
    #
    # """)


def htmltrain(request):
    return render(request, 'home/html-train.html')


def multipage(request, page_id: int):
    print(page_id)
    data = {
        'page__id': page_id,
        'text': 'hello to you',
        'animals': ['cat', 'dog', 'owl', 'fish'],
        'range': range(10)
    }
    return render(request, 'home/multi-value-page.html', context=data)


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, 'home/login.html')
    elif request.method == "POST":
        data = {}

        _login = request.POST.get('login_field')
        _password = request.POST.get('password_field')

        user = authenticate(request, username=_login, password=_password)
        if user is None:
            data['report'] = 'Пользователь не найден или неверный пароль!'
            return render(request, 'home/login.html', context=data)
        else:
            login(request, user)
            return redirect("/")


def logout_user(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, 'home/register.html', context={})
    elif request.method == "POST":
        login = request.POST.get('login_field')
        email = request.POST.get('email_field')
        pass1 = request.POST.get('password_field')
        pass2 = request.POST.get('password_confirm_field')

        data = dict()
        data['login'] = login
        data['email'] = email
        data['pass1'] = pass1
        data['pass2'] = pass2

        if pass1 != pass2:
            report = 'Пароли должны совпадать'
        elif '' in data.values():
            report = 'Все поля - ОБЯЗАТЕЛЬНЫЕ'
        elif len(pass1) < 8:
            report = 'Слишком короткий пароль'
        else:
            user = User.objects.create_user(login, email, pass1)
            user.save()
            if user:
                return redirect("/")
        report = 'Что-то страшное произошло!'
        data['report'] = report
        return render(request, 'home/register.html', context=data)

