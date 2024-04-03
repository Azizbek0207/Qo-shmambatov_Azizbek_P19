from django.shortcuts import render

from apps.models import  CreativeTeam, Director


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
    person = CreativeTeam.objects.all()
    director = Director.objects.all()
    context = {
        'director': director,
        'person': person
    }
    return render(request, 'apps/index.html', context)
