from django.db import models
import random
import os
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db.models.signals import pre_save, post_save



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_user_image(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "user/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class UserManager(BaseUserManager):
    def _create_user(self,  email, password=None, is_staff=False, is_superuser=False, is_admin=False, **extra_fields):
        if not email:
            raise ValueError('Veillez entrer votre adresse email')
        if not password:
            raise ValueError("Veillez entrer votre mot de passe")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            is_admin = is_admin,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(  email,password, False,False,False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(  email,password, True,True,True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email         = models.EmailField(max_length=254, unique=True)
    name          = models.CharField(max_length=254,null = True)
    last_name     = models.CharField(max_length=254,null = True)
    phone_number  = models.CharField(max_length = 15, blank = True )
    #image         = models.ImageField(upload_to=upload_user_image, blank=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    is_admin      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    last_login    = models.DateTimeField(null=True, blank=True)
    date_joined   = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD  = 'email'
    EMAIL_FIELD     = 'email'
    REQUIRED_FIELDS = []

    objects         = UserManager()


