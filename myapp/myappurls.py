from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('form',views.form,name='form'),
    path('add',views.add,name='add'),
    path('delete/(?P<id>\d+)/$',views.delete,name='delete'),
    ]