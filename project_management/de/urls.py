from django.urls import path
from . import views

app_name = 'de'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('main/', views.main_page, name='set_de'),
    path('main/view/<int:id>/', views.view_project, name='view_project'),
    path('main/set_project/', views.set_project, name='set_project'),
    path('api/project/<int:project_id>/', views.get_project_detail_api, name='get_project_detail_api'),
    path('main/delete_project/<int:id>/', views.deleteproject, name='delete_project'),
    path('main/edit_project/<int:id>/', views.editproject, name='edit_project'),

    #Pekerjaan
    path('main/<int:project_id>/set_pekerjaan/', views.set_pekerjaan, name='set_pekerjaan'),
    path('main/view_pekerjaan/<int:id>/', views.view_pekerjaan, name='view_pekerjaan'),
    path('api/pekerjaan/<int:pekerjaan_id>/', views.get_pekerjaan_detail_api, name='get_pekerjaan_detail_api'),
    path('main/delete_pekerjaan/<int:id>/', views.delete_pekerjaan, name='delete_pekerjaan'),
    path('main/edit_pekerjaan/<int:id>/', views.edit_pekerjaan, name='edit_pekerjaan'),

    #Aktivitas
    path('main/<int:pekerjaan_id>/set_aktivitas/', views.set_aktivitas, name='set_aktivitas'),
    path('main/view_aktivitas/<int:id>/', views.view_aktivitas, name='view_aktivitas'),
    path('main/edit_aktivitas/<int:id>/', views.edit_aktivitas, name='edit_aktivitas'),
    path('main/delete_aktivitas/<int:id>/', views.delete_aktivitas, name='delete_aktivitas'),
    path('api/aktivitas/<int:aktivitas_id>/', views.get_aktivitas_detail_api, name='get_aktivitas_detail_api'),

    # API project
    path('api/projects/', views.SemuadataView.as_view(), name='api_projects'),
    path('api/projects/<int:pk>/update/', views.ProjectInfoUpdateView.as_view(), name='update_project_info'),
    path('api/pekerjaan/<int:pk>/update/', views.PekerjaanUpdateView.as_view(), name='update_pekerjaan'),
    path('api/aktivitas/<int:pk>/update/', views.AktivitasUpdateView.as_view(), name='update_aktivitas'),

     # Send project data API path
    path('api/send_project_data/<int:pk>/', views.SendProjectData.as_view(), name='send_project_data'),

]

