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


class user_updateform(forms.ModelForm):
	def __init__ (self , email, *args , **kwargs ):
		super ( user_updateform, self ).__init__(*args,**kwargs)
		self.fields['name'].initial 			    = User.objects.get(email = email).name
		self.fields['last_name'].initial          	= User.objects.get(email = email).last_name
		self.fields['email'].initial   	            = User.objects.get(email = email).email
		self.fields['phone_number'].initial         = User.objects.get(email = email).phone_number
		self.fields['date_joined'].initial         	= User.objects.get(email = email).date_joined
		self.fields['last_login'].initial         	= User.objects.get(email = email).last_login

	email = forms.EmailField(widget =forms.EmailInput(attrs={'disabled':True,}), label='' )
	date_joined = forms.DateTimeField(widget =forms.TextInput(attrs={'disabled':True,}), label='' )
	last_login = forms.DateTimeField(widget =forms.TextInput(attrs={'disabled':True,}), label='' )


	class Meta:
		model = User
		fields = [
        	'name',
        	'last_name',
        	'email',
            'phone_number',
            'role',
            'last_login',    
        ]
