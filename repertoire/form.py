from django import forms


from .models import *

class repertoireform(forms.ModelForm):

    class Meta:
        model = Repertoire
        fields = [
            'nom',
            
        ]


class serieform(forms.ModelForm):

    class Meta:
        model = Serie
        fields = [
            'repertoire',
            'cote',
            'nom',
            
        ]


class sousserieform(forms.ModelForm):

    class Meta:
        model = SousSerie
        fields = [
            'serie',
            'nom',
            
        ]

class divisionform(forms.ModelForm):

    class Meta:
        model = Division
        fields = [
            'sousserie',
            'nom',
            
        ]

class archivesform(forms.ModelForm):

    class Meta:
        model = Archives
        fields = [
            'division',
            'boite',
            'nom',
            'nbrSousDoc',
            'description',
            'dateExtrem_min',
            'dateExtrem_max',
            'dua',
                
        ]

class boitearchiveform(forms.ModelForm):

    class Meta:
        model = Boite_archive
        fields = [
            'numero',
            'emplacement',
            
        ]
