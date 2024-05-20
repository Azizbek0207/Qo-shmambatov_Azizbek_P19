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
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.form import RegisterModelForm
from apps.models import Contact, Position, Member, PositionTag, Blog, Category, Email
from django.utils.translation import gettext as _
from apps.form import VerificationForm

# views.py
from django.shortcuts import render, redirect


class ProductListView(ListView):
    model = Contact
    template_name = 'apps/auth/list.html'
    context_object_name = 'contacts'
    paginate_by = 1


class MemberList(ListView):
    queryset = Member.objects.all()
    template_name = 'apps/auth/member.html'
    context_object_name = 'members'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['tags'] = PositionTag.objects.all()
        return context

    def get_queryset(self):
        res = self.request.GET.get('choices-single-categories')
        search = self.request.GET.get('search')
        queryset = super().get_queryset()

        if res:
            queryset = queryset.filter(job__id=res)
        if search:
            queryset = queryset.filter(first_name__icontains=search)
        return queryset


class ProfileViewPage(LoginRequiredMixin, LoginView):
    template_name = 'apps/auth/profile.html'
    login_url = 'login_page'


class RegisterViewPage(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/auth/register.html'
    success_url = 'login'


def logout_view(request):
    logout(request)
    return redirect('login_page')


class ViewPage(TemplateView, LoginRequiredMixin):
    template_name = 'apps/auth/index.html'
    login_url = 'login_page'


class RegisterPage(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/auth/login-register.html'
    success_url = 'register'


class MainPage(ListView):
    queryset = Blog.objects.all()
    template_name = 'apps/auth/index.html'
    context_object_name = 'blogs'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = super().get_context_data(object_list=object_list, **kwargs)
        queryset['categories'] = Category.objects.all()
        return queryset


class DetailPage(TemplateView):
    template_name = 'apps/auth/detail.html'



