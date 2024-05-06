from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import path

from apps.tasks import send_message
from apps.views import logout_view, \
    RegisterPage, MainPage, DetailPage


def send_email(request):
    msg = request.GET.get('msg')
    send_message.delay(msg)
    return HttpResponse('Hello world')


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='apps/login-register.html',
        next_page='verification',
        redirect_authenticated_user=True,
    ), name='login_page'),
    # path('profile/', ProfileViewPage.as_view(), name='profile_page'),
    # path('register', RegisterViewPage.as_view(), name='register'),3
    path('logout', logout_view, name='logout'),
    path('', MainPage.as_view(), name='home_page'),
    path('register', RegisterPage.as_view(), name='register_page'),
    path('detail/', DetailPage.as_view(), name='detail_page'),
    path('send/', send_email),

]
