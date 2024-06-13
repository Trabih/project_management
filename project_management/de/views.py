from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectForm,AnggotaForm,PekerjaanForm,AktivitasForm
from .models import ProjectInfo,Anggota,Pekerjaan,Aktivitas
from django.http import JsonResponse

def main_page(request):
    list_project = ProjectInfo.objects.all().order_by('-id')
    context = {
        'list_project': list_project,
    }
    return render(request, 'de/de.html', context)


# Create your views here.
def set_project(request):
    list_project = ProjectInfo.objects.all().order_by('-id')  
    context = None
    form = ProjectForm(None)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            list_project = ProjectInfo.objects.all().order_by('-id')
            context = {
              "form": form, 
              "list_project": list_project,
              "ProjectInfo" : ProjectInfo,
              }
            return render(request, 'de/project_de.html', context)
    else:
        list_project = ProjectInfo.objects.all().order_by('-id')
        context = {
            "form": form, 
            "list_project": list_project,
            "ProjectInfo" : ProjectInfo,
            }
        return render(request, "de/project_de.html", context)
    
def view_project(request, id):
    try:
        project = ProjectInfo.objects.get(pk=id)
        return render(request, 'de/project_detail.html', {'project_id': project.id})
    except ProjectInfo.DoesNotExist:
        return JsonResponse({'error': 'project not found'}, status=404)

def get_project_detail_api(request, project_id):
    try:
        project = ProjectInfo.objects.get(pk=project_id)
        data = {
            'nama': project.nama_project,
            'tujuan': project.tujuan_project,
            'tangmul': project.tangmul_project,
            'tangsel': project.tangsel_project,
            'pic': project.pic_project,
            'status': project.status_project,
            'tanggal_add': project.tanggal_add,
        }
        return JsonResponse(data)
    except ProjectInfo.DoesNotExist:
        return JsonResponse({'error': 'project not found'}, status=404)

def deleteproject(request, id):
    project = get_object_or_404(ProjectInfo, pk=id)
    project.delete()
    return redirect('de:set_de')

def editproject(request, id):
    project = get_object_or_404(ProjectInfo, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('de:set_de')
    return render(request, 'de/project_edit.html', {'form': form})

def set_anggota(request, id):
    project = get_object_or_404(ProjectInfo, pk=id)  # Get the project by id
    form = AnggotaForm(None)
    if request.method == 'POST':
        form = AnggotaForm(request.POST)
        if form.is_valid():
            anggota = form.save(commit=False)
            anggota.project = project  # Associate the new anggota with the project
            anggota.save()
            context = {
                "form": form,
                "project": project,
                "success_message": "Anggota added successfully"
            }
            return render(request, 'de/anggota.html', context)
    else:
        context = {
            "form": form,
            "project": project
        }
        return render(request, 'de/anggota.html', context)

def set_pekerjaan(request):
    list_pekerjaan = Pekerjaan.objects.all().order_by('-id')
    context = None
    form = PekerjaanForm(None)
    if request.method == "POST":
        form = PekerjaanForm(request.POST)
        if form.is_valid():
            form.save()
            list_pekerjaan = Pekerjaan.objects.all().order_by('-id')
            context = {
                "form": form,
                "list_pekerjaan": list_pekerjaan,
                "Pekerjaan": Pekerjaan,
            }
            return render(request, 'de/pekerjaan_de.html', context)
    else:
        list_pekerjaan = Pekerjaan.objects.all().order_by('-id')
        context = {
            "form": form,
            "list_pekerjaan": list_pekerjaan,
            "Pekerjaan": Pekerjaan,
        }
        return render(request, "de/pekerjaan_de.html", context)

def get_pekerjaan_detail_api(request, user_id):
    try:
        pekerjaan = Pekerjaan.objects.get(pk=user_id)
        data = {
            'nama_pek': pekerjaan.nama_pek,
            'desk_pek': pekerjaan.desk_pek,
            'tangmul_pek': pekerjaan.tangmul_pek,
            'tempatmul_pek': pekerjaan.tempatmul_pek,
            'tangsel_pek': pekerjaan.tangsel_pek,
            'tempatsel_pek': pekerjaan.tempatsel_pek,
            'pel_pek': pekerjaan.pel_pek,
            'super_pek': pekerjaan.super_pek,
            'status_pek': pekerjaan.status_pek,
        }
        return JsonResponse(data)
    except Pekerjaan.DoesNotExist:
        return JsonResponse({'error': 'Pekerjaan not found'}, status=404)