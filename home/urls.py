from django.urls import path
from .views import index, htmltrain, multipage, sign_in, register, logout_user, ajax_reg

urlpatterns = [
    path('', index, name='homepage'),
    path('html_train', htmltrain, name='htmltrain'),
    path('multi_page/<int:page_id>', multipage, name='multipage'),
    path('login', sign_in, name='login-page'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('ajax_reg', ajax_reg, name='ajax_reg'),
]
