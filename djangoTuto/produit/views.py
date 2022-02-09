from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Produit
from .forms import ProduitForm

def home(request):
    return render(request, "produit/index.html", {})

@staff_member_required
def produit_list(request, template_name='produit/list.html'):
    contact_list = Produit.objects.all()
    paginator = Paginator(contact_list, 10 )
    page = request.GET.get('page')
    try:
        produits = paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    return render(request,template_name, {'produits': produits })

@staff_member_required
def produit_create(request, template_name='produit/produit_form.html'):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        produits = form.save(commit=False)
        produits.user = request.user
        produits.save()
        return redirect('produit:produit_list')
    return render(request, template_name, {'form':form})

@staff_member_required
def produit_update(request, pk, template_name='produit/produit_form.html'):
    if request.user.is_superuser:
        produits= get_object_or_404(Produit, pk=pk)
    else:
        produits= get_object_or_404(Produit, pk=pk, user=request.user)
    form = ProduitForm(request.POST or None, instance=produits)
    if form.is_valid():
        form.save()
        return redirect('produit:produit_list')
    return render(request, template_name, {'form':form})

@staff_member_required
def produit_delete(request, pk, template_name='lab/produit_confirm_delete.html'):
    if request.user.is_superuser:
        produits= get_object_or_404(Produit, pk=pk)
    else:
        produits= get_object_or_404(Produit, pk=pk, user=request.user)
    if request.method=='POST':
        produits.delete()
        return redirect('produit:produit_list')
    return render(request, template_name, {'object':produits})
