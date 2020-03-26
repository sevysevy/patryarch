import datetime 
import os
import random
import string

from django.utils import timezone
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_repertoire_id_generator(instance, repertoire_id=None):
    
    """
    This is for generate an repertoire_id field
    """

    if repertoire_id is not None:
    	repertoire_new_id = repertoire_id 
    else:
    	repertoire_new_id = random_string_generator()
    	Klass = instance.__class__
    	qs_exists = Klass.objects.filter(repertoire_id=repertoire_new_id).exists()
    	if qs_exists:
    		new_id = "{id}-{randstr}".format(
    			id=repertoire_new_id,
    			randstr=random_string_generator(size=4)
    			)
    		return unique_repertoire_id_generator(instance, repertoire_id=new_id)

    	return repertoire_new_id

    return repertoire_new_id

def get_filename(path): #/abc/filename.mp4
    return os.path.basename(path)

