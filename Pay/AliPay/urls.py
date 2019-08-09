from django.urls import path
from . import views

urlpatterns = [

    path('pay', views.pay, name='pay'),
    path('refund', views.refund, name='refund'),
    path('cancel', views.cancel, name='cancel'),
    # path('query', views.query, name='query'),
    path('setting', views.setting, name='setting'),
    path('save_setting', views.save_setting, name='save_setting')
]
