from django.urls import path, include


from . import views

urlpatterns = [
    path('create', views.create_repertoire, name='create_repertoire'),
    path('<repertoire_id>', views.repertoire, name='repertoire_archives'),
    path('<repertoire_id>/dashboard', views.dashboard_repertoire, name='repertoire_dashboard'),
    path('tree_views/', views.tree_views, name='repertoire_tree_views'),

   

    path('create/serie', views.create_serie, name='create_serie'),
    path('detail/serie/<cote>', views.detail_serie, name='detail_serie'),
    path('serie/<cote>/update', views.update_serie, name='update_serie'),
    path('serie/<cote>/delete', views.delete_serie, name='delete_serie'), 

    path('create/sousserie', views.create_sousserie, name='create_sousserie'),
    path('detail/sousserie/<cote>', views.detail_sousserie, name='detail_sousserie'),
    
    path('create/division', views.create_division, name='create_division'),
    path('detail/division/<cote>', views.detail_division, name='detail_division'),

    path('create/archives', views.create_archives, name='create_archives'),
    path('detail/archive/<cote>', views.detail_archive, name='detail_archive'),
    
    path('<repertoire_id>/create/boitearchives', views.create_boitearchive, name='create_boitearchive'),
    #path('')

]
