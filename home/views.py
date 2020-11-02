from django.shortcuts import render, HttpResponse


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
    return render(request, 'home/login.html')


def register(request):
    return render(request, 'home/register.html')
