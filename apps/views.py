from django.contrib.auth import logout
# views.py
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView

from apps.form import RegisterModelForm
from apps.models import Member, User


class MemberList(ListView):
    queryset = Member.objects.all()
    template_name = 'apps/exam/profile.html'
    context_object_name = 'members'
    paginate_by = 2


class RegisterViewPage(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/exam/register.html'
    success_url = '/'


class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'photo']


#
#
#
#
def logout_view(request):
    logout(request)
    return redirect('login_page')
#

#
