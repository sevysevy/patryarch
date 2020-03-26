from django.urls import path, include


from . import views

urlpatterns = [
    path('create', views.create_repertoire, name='create_repertoire'),
    path('<repertoire_id>', views.repertoire, name='repertoire_archives'),
    path('<repertoire_id>/dashboard', views.dashboard_repertoire, name='repertoire_dashboard'),
    path('tree_views/', views.tree_views, name='repertoire_tree_views'),
    path('create/serie', views.create_serie, name='create_serie'),
    path('create/sousserie', views.create_sousserie, name='create_sousserie'),
    path('create/division', views.create_division, name='create_division'),
    path('create/archives', views.create_archives, name='create_archives'),
    path('<repertoire_id>/create/boitearchives', views.create_boitearchive, name='create_boitearchive'),
    #path('')

]
