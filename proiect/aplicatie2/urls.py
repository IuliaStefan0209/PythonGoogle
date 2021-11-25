from django.urls import path
from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns = [
    path('', views.CreateLocationView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modificare'),
    path('list/', views.ListLocationView.as_view(), name='listare')
]