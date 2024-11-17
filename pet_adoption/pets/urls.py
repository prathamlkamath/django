from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('details/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('<int:pet_id>/adopt-form/', views.adoption_form, name='adoption_form'),
    path('<int:pet_id>/adopt/', views.adopt_pet, name='adopt_pet'),
]
