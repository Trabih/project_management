from django.urls import path
from .import views

urlpatterns =[
    path('de/', views.set_de, name = 'set_de'),
    path('de/view/<id>', views.view_project, name='view_project'),
    path('api/project/<int:user_id>/', views.get_project_detail_api, name = 'get_project_detail_api'),
    path('deleteproject/<int:id>/',views.deleteproject,name = 'delete_project'),
    path('editproject/<int:id>/',views.editproject,name = 'edit_project'),
    path('set_anggota/<int:id>/',views.set_anggota,name='set_anggota'),
]