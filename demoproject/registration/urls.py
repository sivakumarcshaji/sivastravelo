from . import views
from django.urls import path
app_name='registration'

urlpatterns = [
    path('show', views.show, name='show'),
    path('log', views.log, name='log'),
    path('logout',views.logout,name='logout')
]
