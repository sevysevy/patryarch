from django.urls import path, include


from . import views

urlpatterns = [
    path('create', views.create_repertoire, name='create_repertoire'),
    path('<repertoire_id>', views.repertoire, name='repertoire_archives'),
    path('<repertoire_id>/dashboard', views.dashboard_repertoire, name='repertoire_dashboard'),
    path('tree_views/', views.tree_views, name='repertoire_tree_views'),

   

    path('create/serie', views.create_serie, name='create_serie'),
    path('serie/<cote>/detail', views.detail_serie, name='detail_serie'),
    path('serie/<cote>/update', views.update_serie, name='update_serie'),
    path('serie/<cote>/delete', views.delete_serie, name='delete_serie'), 

    path('create/sousserie', views.create_sousserie, name='create_sousserie'),
    path('serie/<cote>/add/sousserie', views.add_sousserie_to, name='add_sousserie'),
    path('sousserie/<cote>/detail', views.detail_sousserie, name='detail_sousserie'),
    path('sousserie/<cote>/update', views.update_sousserie, name='update_sserie'),
    path('sousserie/<cote>/delete', views.delete_sousserie, name='delete_sserie'), 
    
    path('create/division', views.create_division, name='create_division'),
    path('sousserie/<cote>/add/division', views.add_division_to, name='add_division'),
    path('division/<cote>/detail', views.detail_division, name='detail_division'),


    path('create/archives', views.create_archives, name='create_archives'),
    path('detail/archive/<cote>', views.detail_archive, name='detail_archive'),
    
    path('<repertoire_id>/create/boitearchives', views.create_boitearchive, name='create_boitearchive'),
    #path('')

]
