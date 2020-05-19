from django import forms


from .models import *

class repertoireform(forms.ModelForm):

    class Meta:
        model = Repertoire
        fields = [
            'nom',
            'description',
            
        ]

class repertoire_updateform(forms.ModelForm):
    description = forms.CharField(widget = forms.TextInput(attrs={'class':'input-text'}), label='', required = False)
    class Meta:
        model = Repertoire
        fields = [
            'nom',
            'description',
        ]


class serieform(forms.ModelForm):


    class Meta:
        model = Serie
        fields = [
            'cote',
            'nom',
        ]


class sousserieform(forms.ModelForm):

    def __init__ (self , repertoire_id, *args , **kwargs ):
        super ( sousserieform, self ).__init__(*args,**kwargs)
        self.fields['serie'].queryset = Serie.objects.filter(repertoireID = repertoire_id)

    class Meta:
        model = SousSerie
        fields = [
            'serie',
            'cote',
            'nom',
            
        ]

class m_sousserieform(forms.ModelForm):

    class Meta:
        model = SousSerie
        fields = [
            'numero',
            'nom',
            
        ]

class divisionform(forms.ModelForm):

    def __init__ (self , repertoire_id, *args , **kwargs ):
        super ( divisionform, self ).__init__(*args,**kwargs)
        self.fields['sousserie'].queryset = SousSerie.objects.filter(repertoireID = repertoire_id)

    class Meta:
        model = Division
        fields = [
            'sousserie',
            'cote',
            'nom',
            
        ]

class m_divisionform(forms.ModelForm):

    class Meta:
        model = Division
        fields = [
            'numero',
            'nom',
            
        ]


class archivesform(forms.ModelForm):
    def __init__ (self , repertoire_id, *args , **kwargs ):
        super ( archivesform, self ).__init__(*args,**kwargs)
        self.fields['division'].queryset = Division.objects.filter(repertoireID = repertoire_id)

    class Meta:
        model = Archives
        fields = [
            'division',
            'boite',
            'cote',
            'nom',
            'nbrSousDoc',
            'description',
            'dateExtrem_min',
            'dateExtrem_max',
            'dua',
                
        ]

class m_archiveform(forms.ModelForm):

    class Meta:
        model = Archives
        fields = [
            'boite',
            'nom',
            'numero',
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
