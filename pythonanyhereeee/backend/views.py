from django.shortcuts import render, redirect
from .models import Produit
from .forms import ProduitForm

# Create your views here.

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    
    return render(request, 'ajouter_produit.html', {'form': form})

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'liste_produits.html', {'produits': produits})
