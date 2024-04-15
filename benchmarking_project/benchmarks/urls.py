from django.urls import path

from . import views
app_name = 'benchmarks'  # creates a namespace for this app
urlpatterns = [
    path('', views.index, name='index'),
]
