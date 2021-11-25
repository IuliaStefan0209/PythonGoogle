from django.urls import path
from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns = [
    path('', views.CreateLocationView.as_view(), name='adaugare')
]