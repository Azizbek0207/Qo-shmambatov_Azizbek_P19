from datetime import timedelta
from random import randint
from time import timezone

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.views import LoginView
from django.contrib.postgres.aggregates import ArrayAgg
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.form import RegisterModelForm
# from apps.models import Contact, Position, Member, PositionTag, Blog, Category, Email
from django.utils.translation import gettext as _
from apps.form import VerificationForm

# views.py
from django.shortcuts import render, redirect

from apps.models import Member


# class ProductListView(ListView):
#     model = Contact
#     template_name = 'apps/auth/list.html'
#     context_object_name = 'contacts'
#     paginate_by = 1
#
#
class MemberList(ListView):
    queryset = Member.objects.all()
    template_name = 'apps/exam/profile.html'
    context_object_name = 'members'
    paginate_by = 2


class RegisterViewPage(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/exam/register.html'
    success_url = '/'


#
class ProfileViewPage(LoginRequiredMixin, LoginView, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'apps/exam/profile.html'
    login_url = 'login_page'


#
#
#
#
def logout_view(request):
    logout(request)
    return redirect('login_page')
#
#
# class ViewPage(TemplateView, LoginRequiredMixin):
#     template_name = 'apps/auth/index.html'
#     login_url = 'login_page'
#
#
# class RegisterPage(CreateView):
#     form_class = RegisterModelForm
#     template_name = 'apps/auth/login-register.html'
#     success_url = 'register'
#
#
# class MainPage(ListView):
#     queryset = Blog.objects.all()
#     template_name = 'apps/auth/index.html'
#     context_object_name = 'blogs'
#     paginate_by = 1
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         queryset = super().get_context_data(object_list=object_list, **kwargs)
#         queryset['categories'] = Category.objects.all()
#         return queryset
#
#
# class DetailPage(TemplateView):
#     template_name = 'apps/auth/detail.html'
#
