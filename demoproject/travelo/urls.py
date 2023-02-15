from . import views
from django.urls import path
app_name = 'travelo'

urlpatterns = [

    path('',views.trvl,name='trvl'),


]
