from django.urls import path

from apps.views import form_view, form_view_detal, index_view, suc_view

urlpatterns = [
    path('detail/<int:pk>', form_view_detal, name='form_view_detail'),
    path('', form_view, name='form_view_list'),
    path('suc/', suc_view, name='success_page'),
    # path('form', form_view, name='form_view'),
    # path('form/<int:pk>', form_view, name='profile_detail_view'),
]
