from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LabForm
from .models import Lab


def home(request):
    return render(request, "lab/index.html", {})


@staff_member_required
def lab_list(request, template_name='lab/list.html'):
    contact_list = Lab.objects.all()
    paginator = Paginator(contact_list, 10)
    page = request.GET.get('page')
    try:
        labs = paginator.page(page)
    except PageNotAnInteger:
        labs = paginator.page(1)
    except EmptyPage:
        labs = paginator.page(paginator.num_pages)
    return render(request, template_name, {'labs': labs})


@staff_member_required
def lab_create(request, template_name='lab/lab_form.html'):
    form = LabForm(request.POST or None)
    if form.is_valid():
        labs = form.save(commit=False)
        labs.user = request.user
        labs.save()
        return redirect('lab:lab_list')
    return render(request, template_name, {'form': form})


@staff_member_required
def lab_update(request, pk, template_name='lab/lab_form.html'):
    if request.user.is_superuser:
        labs = get_object_or_404(Lab, pk=pk)
    else:
        labs = get_object_or_404(Lab, pk=pk, user=request.user)
    form = LabForm(request.POST or None, instance=labs)
    if form.is_valid():
        form.save()
        return redirect('lab:lab_list')
    return render(request, template_name, {'form': form})


@staff_member_required
def lab_delete(request, pk, template_name='lab/lab_confirm_delete.html'):
    if request.user.is_superuser:
        labs = get_object_or_404(Lab, pk=pk)
    else:
        labs = get_object_or_404(Lab, pk=pk, user=request.user)
    if request.method == 'POST':
        labs.delete()
        return redirect('lab:lab_list')
    return render(request, template_name, {'object': labs})
