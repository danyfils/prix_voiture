from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib

def voiture(request):
    template=loader.get_template('base.html')
    return HttpResponse(template.render({},request))

def predict(request):
    #on verifie si la methode est POST pour
    #recuperer les donnees du formulaire
    if request.method=='POST':

        #on garde dans les varialbes les valeurs
        #venues des champs du formulaire
        #on les convertit en entier car le formulaire
        #retourne par defaut les chaines de caracteres
        nb_places=int(request.POST['nb_places'])
        nb_porte=int(request.POST['nb_porte'])
        automatique=int(request.POST['automatique'])
        

        #on cree un table en deux dimensions pour le soumettre
        #au modele de prediction
        tableau=[[nb_places,nb_porte,automatique]]
        print(tableau)

        #on charge le modele
        regresseur=joblib.load('modele_ml/ml_prix-voiture.pkl')
        resultat=regresseur.predict(tableau)
        
        print(resultat)
        


    return HttpResponse('ok')