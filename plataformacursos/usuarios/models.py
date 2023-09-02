from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def _create_user(self,email,username,nombre,apellido,password,is_staff, is_superuser,**extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombre = nombre, 
            apellido = apellido,
            is_superuser = is_superuser,
            is_staff = is_staff,
            **extra_fields,
        )
        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario
    
    def create_user(self,email,username,nombre,apellido,password=None, **extra_fields):
        print(self)
        print(**extra_fields)
        return self._create_user(email,username,nombre,apellido,password,True, False,**extra_fields)
    
    def create_superuser(self,email,username,nombre,apellido,password=None, **extra_fields):
        return self._create_user(email,username,nombre,apellido,password,True, True,**extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=20, null=False, blank=False)
    foto = models.ImageField('Foto de perfil', upload_to='usuarios/',max_length=255,default='default.png')
    c_id = models.CharField('Cedula', max_length=10, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    direccion = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    fecha_create = models.DateField(default=datetime.today())
    is_staff = models.BooleanField(default=False)
    object = UsuarioManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre','apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']