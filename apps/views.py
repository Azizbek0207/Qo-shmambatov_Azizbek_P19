from django.shortcuts import render

from apps.models import  ContactsPage


#
#
# # Create your views here.
# def index_view(request):
#     product = Product.objects.all()
#     context = {
#         'product': product
#     }
#     return render(request, 'apps/index.html', context)
#
#
# def detail_view(request):
#     product = Product.objects.all()
#     context = {
#         'product': product
#     }
#     return render(request, 'apps/detail.html', context)


def index_view(request):
    contacts = ContactsPage.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'apps/index.html', context)
