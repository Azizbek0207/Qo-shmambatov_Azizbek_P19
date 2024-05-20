from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import path

from apps import views
# from apps.tasks import send_message
from apps.views import MemberList, RegisterViewPage, UserUpdateView


def send_email(request):
    msg = request.GET.get('msg')
    # send_message.delay(msg)
    return HttpResponse('Hello world')


urlpatterns = [
    path('', MemberList.as_view(), name='memberlist'),
    path('login/', LoginView.as_view(
        template_name='apps/exam/login.html',
        next_page='profile',
        redirect_authenticated_user=True,
    ), name='login_page'),
    path('register/', RegisterViewPage.as_view(), name='register'),
    path('profile/<int:pk>', UserUpdateView.as_view(), name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
