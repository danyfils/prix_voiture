
from django.urls import path
from . import views

urlpatterns=[
    path('voiture/',views.voiture,name='voiture'),
   # path('liste/',views.listeEtudiants,name="liste"),
    #path('prix/',views.voiture,name='prix'),
    path('predict/',views.predict,name='predire')
]