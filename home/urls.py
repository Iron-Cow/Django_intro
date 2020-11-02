from django.urls import path
from .views import index, htmltrain, multipage, sign_in, register

urlpatterns = [
    path('', index, name='homepage'),
    path('html_train', htmltrain, name='htmltrain'),
    path('multi_page/<int:page_id>', multipage, name='multipage'),
    path('login', sign_in, name='login-page'),
    path('register', register, name='register')
]
