from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.mail import send_mail

from apps.models import Blog, Category, User
from root.settings import EMAIL_HOST_USER


#
#
# # Create your views here.
def index_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        User.objects.create(first_name=first_name, last_name=last_name)
    return render(request, 'apps/index.html')

#
# def detail_view(request, pk):
#     users = User.objects.get(pk=pk)
#     context = {
#         'users': users
#     }
#     return render(request, 'apps/form.html', context)


def form_view(request):
    blog = Blog.objects.all()
    category = Category.objects.all()
    context = {
        "blog": blog,
        "category": category
    }
    return render(request, 'apps/list.html', context)


def form_view_detal(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        "blog1": blog
    }
    return render(request, 'apps/detail.html', context)


# def form_view_detail_update(request, pk):
#     blog = Blog.objects.get(pk=pk)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         image = request.POST.get('image')
#
#         blog.name = name
#         blog.description = description
#         blog.image = image
#         Blog.save(blog)
#         return redirect('index_menu_view')
#
#     context = {
#         'blog1': blog
#     }
#     return render(request, 'apps/index.html', context)


# def form_detail_delete(request, pk):
#     if request.method == 'POST':
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return render(request, 'apps/index.html')
#     else:
#         return render(request, 'apps/form.html')


def suc_view(req):
    return render(req, 'apps/success.html')
