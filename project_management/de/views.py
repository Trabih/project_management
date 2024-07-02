from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import ProjectInfo, Pekerjaan,Aktivitas
from .forms import ProjectForm, PekerjaanForm, AktivitasForm
import requests
from .serializers import *
from django.http import JsonResponse
from rest_framework import generics
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum 
from rest_framework.decorators import api_view

def main_page(request):
    list_project = ProjectInfo.objects.all().order_by('-id')
    context = {
        'list_project': list_project,
    }
    return render(request, 'de/de.html', context)

def set_project(request):
    list_project = ProjectInfo.objects.all().order_by('-id')
    form = ProjectForm(None)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            #kirim_ke_IE(project)
            return redirect('de:main_page')
    context = {
        "form": form,
        "list_project": list_project,
    }
    return render(request, "de/project_de.html", context)

def view_project(request, id):
    project = get_object_or_404(ProjectInfo, pk=id)
    list_pekerjaan = Pekerjaan.objects.filter(project=project)
    context = {
        'project': project,
        'list_pekerjaan': list_pekerjaan,
    }
    return render(request, 'de/project_detail.html', context)

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
            'biaya': project.biaya,
        }
        return JsonResponse(data)
    except ProjectInfo.DoesNotExist:
        return JsonResponse({'error': 'project not found'}, status=404)

def deleteproject(request, id):
    project = get_object_or_404(ProjectInfo, pk=id)
    project.delete()
    return redirect('de:main_page')

def editproject(request, id):
    project = get_object_or_404(ProjectInfo, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('de:main_page')
    return render(request, 'de/project_edit.html', {'form': form})


def archived_projects(request):
    archived_projects = ProjectInfo.objects.filter(is_archived=True)
    context = {
        'archived_projects': archived_projects
    }
    return render(request, 'de/archived_projects.html', context)

def archive_project_confirmation(request, project_id):
    project = get_object_or_404(ProjectInfo, pk=project_id)
    if request.method == "POST":
        signature_picture = request.FILES.get('signature_picture')
        if signature_picture:
            project.signature_picture = signature_picture

        # Mark the project as archived  
        project.is_archived = True
        project.save()
        return redirect('de:main_page')

    context = {
        'project': project
    }
    return render(request, 'de/archive_confirmation.html', context)



def set_pekerjaan(request, project_id):
    project = get_object_or_404(ProjectInfo, pk=project_id)
    form = PekerjaanForm(None)
    if request.method == "POST":
        form = PekerjaanForm(request.POST)
        if form.is_valid():
            pekerjaan = form.save(commit=False)
            pekerjaan.project = project
            pekerjaan.save()
            redirect_url = 'de:view_project'
            update_project_biaya(project)
            print(f"Redirecting to: {redirect_url}, with id: {project.id}")
            return redirect(redirect_url, id=project.id)
    context = {
        'form': form,
        'project': project
    }
    return render(request, 'de/pekerjaan_de.html', context)


def view_pekerjaan(request, id):
    pekerjaan = get_object_or_404(Pekerjaan, pk=id)
    context = {
        'pekerjaan': pekerjaan
    }
    return render(request, 'de/pekerjaan_detail.html', context)

def get_pekerjaan_detail_api(request, pekerjaan_id):
    try:
        pekerjaan = get_object_or_404(Pekerjaan, pk=pekerjaan_id)
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
            'biaya_pek': pekerjaan.biaya_pek,
        }
        return JsonResponse(data)
    except Pekerjaan.DoesNotExist:
        return JsonResponse({'error': 'pekerjaan not found'}, status=404)

def delete_pekerjaan(request, id):
    pekerjaan = get_object_or_404(Pekerjaan, pk=id)
    pekerjaan.delete()
    return redirect('de:main_page')

def edit_pekerjaan(request, id):
    pekerjaan = get_object_or_404(Pekerjaan, pk=id)
    form = PekerjaanForm(request.POST or None, instance=pekerjaan)
    if form.is_valid():
        form.save()
        update_project_biaya(pekerjaan.project)
        return redirect('de:view_project', id=pekerjaan.project.id)
    return render(request, 'de/pekerjaan_edit.html', {'form': form})

def set_aktivitas(request, pekerjaan_id):
    pekerjaan = get_object_or_404(Pekerjaan, pk=pekerjaan_id)
    form = AktivitasForm()
    if request.method == "POST":
        form = AktivitasForm(request.POST)
        if form.is_valid():
            aktivitas = form.save(commit=False)
            aktivitas.pekerjaan = pekerjaan
            aktivitas.save()
            redirect_url = 'de:view_pekerjaan'
            update_pekerjaan_biaya(pekerjaan)
            return redirect(redirect_url, id=pekerjaan.id)
    context = {
        'form': form,
        'pekerjaan': pekerjaan
    }
    return render(request, 'de/aktivitas_de.html', context)

def view_aktivitas(request, id):
    aktivitas = get_object_or_404(Aktivitas, pk=id)
    context = {
        'aktivitas': aktivitas
    }
    return render(request, 'de/aktivitas_detail.html', context)

def edit_aktivitas(request, id):
    aktivitas = get_object_or_404(Aktivitas, pk=id)
    form = AktivitasForm(request.POST or None, instance=aktivitas)
    if form.is_valid():
        form.save()
        update_pekerjaan_biaya(aktivitas.pekerjaan)
        return redirect('de:view_pekerjaan', id=aktivitas.pekerjaan.id)
    return render(request, 'de/aktivitas_edit.html', {'form': form})

def delete_aktivitas(request, id):
    aktivitas = get_object_or_404(Aktivitas, pk=id)
    pekerjaan_id = aktivitas.pekerjaan.id
    aktivitas.delete()
    return redirect('de:view_pekerjaan', id=pekerjaan_id)

def get_aktivitas_detail_api(request, aktivitas_id):
    try:
        aktivitas = get_object_or_404(Aktivitas, pk=aktivitas_id)
        data = {
            'nama_akti': aktivitas.nama_akti,
            'wakpel_akti': aktivitas.wakpel_akti,
            'pel_akti': aktivitas.pel_akti,
            'eval_akti': aktivitas.eval_akti,
            'ren_akti': aktivitas.ren_akti,
            'status_akti': aktivitas.status_akti,
            'biaya_akti': aktivitas.biaya_akti,
        }
        return JsonResponse(data)
    except Aktivitas.DoesNotExist:
        return JsonResponse({'error': 'Aktivitas not found'}, status=404)
    
def update_pekerjaan_biaya(pekerjaan):
    total_biaya = pekerjaan.aktivitas.aggregate(total=Sum('biaya_ak'))['total'] or 0.00
    pekerjaan.biaya = total_biaya
    pekerjaan.save()
    update_project_biaya(pekerjaan.project)

def update_project_biaya(project):
    total_biaya = project.pekerjaan.aggregate(total=Sum('biaya_pek'))['total'] or 0.00
    project.biaya = total_biaya
    project.save()

#API

class SemuadataView(APIView):
    def get(self, request, *args, **kwargs):
        projects = ProjectInfo.objects.all()
        projects_serializer = ProjectInfoSerializer(projects, many=True)

        pekerjaan = Pekerjaan.objects.all()
        pekerjaan_serializer = PekerjaanSerializer(pekerjaan, many=True)

        aktivitas = Aktivitas.objects.all()
        aktivitas_serializer = AktivitasSerializer(aktivitas, many=True)

        combined_data = {
            'projects': projects_serializer.data,
            'pekerjaan': pekerjaan_serializer.data,
            'aktivitas': aktivitas_serializer.data,
        }

        return Response(combined_data)
    
class ProjectInfoDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoUpdateSerializer

class PekerjaanDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pekerjaan.objects.all()
    serializer_class = PekerjaanUpdateSerializer

class AktivitasDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Aktivitas.objects.all()
    serializer_class = AktivitasUpdateSerializer

    
@api_view(['POST'])
def notify_project_deployment(request, pk):
    project = get_object_or_404(ProjectInfo, pk=pk)
    response = requests.post('http://implementation_module/api/notify/', json={
        'project_name': project.nama_project,
        'message': 'Project is ready to be deployed.'
    })

    if response.status_code == 201:
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'error', 'details': response.json()}, status=status.HTTP_400_BAD_REQUEST)
