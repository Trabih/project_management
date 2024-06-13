from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('main/', views.main_page, name='set_de'),  # Fix the name parameter here
    path('main/view/<int:id>/', views.view_project, name='view_project'),
    path('main/set_project/', views.set_project, name='set_project'),  # Fix the name parameter here
    path('api/project/<int:project_id>/', views.get_project_detail_api, name='get_project_detail_api'),
    path('deleteproject/<int:id>/', views.deleteproject, name='delete_project'),
    path('editproject/<int:id>/', views.editproject, name='edit_project'),

    path('set_anggota/<int:id>/', views.set_anggota, name='set_anggota'),
    
    path('main/set_pekerjaan/', views.set_pekerjaan, name='set_pekerjaan'),
    path('api/pekerjaan/<int:pekerjaan_id>/', views.get_project_detail_api, name='get_pekerjaan_detail_api'),
]
