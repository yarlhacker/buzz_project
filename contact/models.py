from django.db import models
from siteweb.models import BaseField

class InfoContact(BaseField):
    tilte = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='images')
    tilte2 = models.CharField(max_length=200)
    description2 = models.TextField()
    
    class Meta:
        verbose_name = 'InfoContact'
        verbose_name_plural = 'InfoContacts'

    def __str__(self):
        return self.tilte


class Contact(BaseField):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=255)
    company_name= models.CharField( max_length=255)
    sujet = models.CharField( max_length=50)
    message = models.TextField()

  
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class TeamContact(BaseField):
    icon = models.CharField(max_length=200)
    domaine = models.CharField(max_length=255)
    personne = models.CharField(max_length=255)
    number= models.CharField( max_length=255)
    
    class Meta:
        verbose_name = 'TeamContact'
        verbose_name_plural = 'TeamContact'

    def __str__(self):
        return self.personne

class Newsletters(BaseField):
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name = 'Newsletters'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email

# Create your models here.