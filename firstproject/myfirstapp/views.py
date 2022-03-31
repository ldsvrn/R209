from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def formulaire(request):
    return render(request, "formulaire.html")

def main(request):
    return render(request, "main.html")

def bonjour(request):
    nom=request.GET["nom"] # récupère la valeur du paramètre nom du formulaire
    age=request.GET["age"]
    return render(request,'bonjour.html', {"nom":nom, "age": age}) # passe cette valeur à la vue au travers du dictionnaire de contexte