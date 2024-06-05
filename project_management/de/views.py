from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectForm,AnggotaForm
from .models import ProjectInfo,Anggota
from django.http import JsonResponse

# Create your views here.
def set_de(request):
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
            return render(request, 'de/de.html', context)
    else:
        list_project = ProjectInfo.objects.all().order_by('-id')
        context = {
            "form": form, 
            "list_project": list_project,
            "ProjectInfo" : ProjectInfo,
            }
        return render(request, "de/de.html", context)
    
def view_project(request, id):
  try:
    project = ProjectInfo.objects.get(pk=id)
    return render(request, 'de/project_detail.html', {'user_id': project.id})
  except ProjectInfo.DoesNotExist:
    return JsonResponse({'error' : 'user not found '}, status = 404)
  
def get_project_detail_api(request, user_id):
    try :
        project = ProjectInfo.objects.get(pk=user_id)
        data = {
        'nama' : project.nama_project,
        'tujuan' : project.tujuan_project,
        'tangmul' : project.tangmul_project,
        'tangsel' : project.tangsel_project,
        'pic' : project.pic_project,
        'status' : project.status_project,
        'tangadd' : project.tanggal_add,
        }
        return JsonResponse(data)
    except ProjectInfo.DoesNotExist:
        return JsonResponse({'error' : 'user not found'}, status=404)

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
