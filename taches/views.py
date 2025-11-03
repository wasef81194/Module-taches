from django.shortcuts  import render
from .forms import TacheForm
from .models import Tache
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    taches = Tache.objects.all()
    return render(request,'taches/home.html', {'taches' : taches})

def new(request):
    response = None
    form = TacheForm()
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            # Crée une instance du modèle sans sauvegarder (commit=False)
            tache = form.save(commit=False)
            tache.title = tache.title.capitalize()
            print('Enregistrement en bdd')
            tache.save()  # Enregistre en BDD !
            form = TacheForm() # Reset le formulaire
            response =  {"bool": True, "message" : "Enregistrement éffectuer avec succées" }
        else :
            response =  {"bool": False, "message" : "Le formulaire n'est pas valide veuilliez saisir tout les champs correctement" } 
    return render(request,'taches/new.html', {'form':form, 'response': response})

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        objet_id = request.POST.get('id')  # Récupère l'id envoyé en POST
        objet = get_object_or_404(Tache, id=objet_id)
        objet.delete()
        return JsonResponse({'success': True, 'message': 'Tache supprimé'})
    else:
        return JsonResponse({'success': False, 'message': 'Méthode non autorisée'}, status=405)
    
