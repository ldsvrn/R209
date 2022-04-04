from django.urls import path
from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('show/', views.show),
    path('read/<int:id>/', views.read),
    path('update/<int:id>/',views.update),
    path('updatedb/<int:id>/',views.updatedb)
]