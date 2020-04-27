from django import forms

from .models import *

class userform(forms.ModelForm):

    class Meta:
        model = User
        fields = [
        	'email',
            'name',
            'last_name',
            'phone_number',
        
            
        ]