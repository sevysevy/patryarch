from django.contrib import admin
from .form import Repertoire,Serie,SousSerie,Division,Archives,Boite_archive 

# Register your models here.

admin.site.register(Repertoire)
admin.site.register(Serie)
admin.site.register(SousSerie)
admin.site.register(Division)
admin.site.register(Archives)
admin.site.register(Boite_archive)
