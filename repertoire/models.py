from datetime import date
#from django.urls import reverse
#from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save, post_save
from patryarch.utils import unique_repertoire_id_generator
#from django.contrib.auth.models import User,Group
#from django.contrib.auth import get_user_model

#LES MODELS DU REPERTOIRE : REPERTOIRE SERIE SOUS-SERIE DIVISION ARCHIVES

#def get_sentinel_user():
 #   return get_user_model().objects.get_or_create(username='Utilisateur Supprimer')[0]

class Repertoire(models.Model):
    repertoire_id      = models.CharField(max_length=20 , unique=True)
    nom                = models.CharField (max_length = 200)
    description        = models.TextField(default='')
    #admin             = models.ManyToManyField(User)
    #Proprietaire      = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user),default=1)

    def __str__(self):
        return '%s' % (self.nom )

def repertoire_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.repertoire_id:
        instance.repertoire_id = unique_repertoire_id_generator(instance)

pre_save.connect(repertoire_pre_save_receiver, sender=Repertoire)



class Serie(models.Model):
    repertoire = models.ForeignKey(Repertoire, on_delete=models.CASCADE)

    cote       = models.CharField(max_length=1) # une lettre de l'alphabet
    nom        = models.CharField(max_length=200)
    
    tag        = models.CharField(max_length=10,default="serie")            #Utiliser par treeviewJS pour l'affichage du repertoire
    repertoireID      = models.CharField(max_length=20,default='')
    #creer_par  = c*z""""""""""""             kmodels.ForeignKey(User, on_delete=models.SET(get_sentinel_user),default=1)

    def __str__(self):
        return '%s -- %s' % (self.cote, self.nom )




class SousSerie(models.Model):
    serie     = models.ForeignKey(Serie, on_delete=models.CASCADE)

    cote      = models.CharField(max_length=10 ) # de la forme A-2
    numero    = models.PositiveIntegerField(default=0)
    nom       = models.CharField(max_length=200)

    tag       = models.CharField(max_length=10,default="sousserie") #Utiliser par treeviewJS pour l'affichage du repertoire
    repertoireID    = models.CharField(max_length=20,default='')
    #creer_par = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user),default=1)

    def __str__(self):
        return '%s -- %s' % (self.cote, self.nom )



def sous_serie_pre_save_receiver(sender, instance, *args, **kwargs):#on determine la cote de la sous serie de maniere automatique
    if not instance.cote:
        serie = instance.serie
        ss = serie.sousserie_set.last()

        if ss == None:
            instance.cote = instance.serie.cote + '-1'
            instance.numero = 1
        else:
            num = ss.numero + 1
            instance.cote = instance.serie.cote + '-'+ str(num)
            instance.numero = num



pre_save.connect(sous_serie_pre_save_receiver, sender=SousSerie)


class Division(models.Model):
    sousserie  = models.ForeignKey(SousSerie, on_delete=models.CASCADE)

    cote       = models.CharField(max_length=20)
    numero     = models.PositiveIntegerField(default=0)
    nom        = models.CharField(max_length=200)
    nombre_arc = models.PositiveIntegerField(default=0)

    tag        = models.CharField(max_length=10,default="division")
    repertoireID    = models.CharField(max_length=20,default='')
    #creer_par  = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user),default=1)


    def __str__(self):
        return '%s -- %s' % (self.cote, self.nom )


def division_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.cote:
        sousserie = instance.sousserie
        div = sousserie.division_set.last()
        if div == None:
            instance.cote = instance.sousserie.cote + '-100'
            instance.numero = 100
        else:
            num = div.numero + 100
            instance.cote = instance.sousserie.cote + '-' + str(num)
            instance.numero = num


pre_save.connect(division_pre_save_receiver, sender=Division)



class Archives(models.Model):
    division         = models.ForeignKey('Division', on_delete=models.CASCADE)
    boite            = models.ForeignKey('Boite_archive', on_delete=models.CASCADE)

    cote             = models.CharField(max_length=30 )
    numero           = models.PositiveIntegerField(default=0)
    nom              = models.CharField(max_length=200)
    description      = models.TextField(null=True)
    dateAjout        = models.DateField(default=date.today)
    present          = models.BooleanField(default=True)
    nbrSousDoc       = models.PositiveIntegerField(default=1)
    dateExtrem_min   = models.DateField()
    dateExtrem_max   = models.DateField()
    dua              = models.DateField()

    tag              = models.CharField(max_length=10,default="archive")
    repertoireID    = models.CharField(max_length=20,default='')
    #creer_par        = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user),default=1)

    def __str__(self):
        return '%s -- %s' % (self.cote, self.nom )

    #def get_absolute_url(self):
        #return reverse('ArchiveDetail', kwargs={'pk': self.pk})


#class Pret(models.Model):
#    archive = models.ForeignKey(Archives, on_delete=models.CASCADE,default=1)
#    preteur = models.CharField( max_length = 50)
#    contact = models.CharField( max_length = 14)
#    date = models.DateField(auto_now_add = True)



def archives_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.cote:
        division = instance.division
        arch = division.archives_set.last()
        if arch == None:
            instance.cote = instance.division.cote + '-001'
            instance.numero = 1
        else:
            num = arch.numero + 1
            instance.cote = instance.division.cote + '-00' + str(num)
            instance.numero = num
        nbr = instance.boite.nombre_doc
        instance.boite.nombre_doc = nbr + 1


pre_save.connect(archives_pre_save_receiver, sender=Archives)



class Boite_archive(models.Model):
    numero = models.PositiveIntegerField(unique = True)
    nombre_doc = models.PositiveIntegerField(default = 0)
    emplacement = models.TextField()
    repertoire = models.ForeignKey(Repertoire, on_delete = models.CASCADE)

    def __str__(self):
        return '%s--%s' % (self.numero, self.nombre_doc)


