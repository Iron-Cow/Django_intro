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
