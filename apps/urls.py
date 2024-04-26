from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import ProductListView, MemberList, ProfileViewPage, RegisterViewPage, logout_view, \
    ViewPage, RegisterPage, MainPage, DetailPage

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='apps/login-register.html',
        next_page='home_page',
        redirect_authenticated_user=True,
    ), name='login_page'),
    # path('profile/', ProfileViewPage.as_view(), name='profile_page'),
    # path('register', RegisterViewPage.as_view(), name='register'),
    # path('logout', logout_view, name='logout'),
    path('', MainPage.as_view(), name='home_page'),
    path('register', RegisterPage.as_view(), name='register_page'),
    path('detail/', DetailPage.as_view(), name='detail_page')
]
