from django.db import models
from siteweb.models import BaseField

class CategorieService(BaseField):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'CategorieService'
        verbose_name_plural = 'CategorieServices'

    def __str__(self):
        return self.name


class Service(BaseField):
    titre = models.CharField(max_length=250)
    image = models.FileField(upload_to='images')
    description = models.TextField()
    categorie = models.ForeignKey("service.CategorieService", on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.titre


class PricingInfo(BaseField):

    image = models.FileField(upload_to='images')
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()

    
    class Meta:
        verbose_name = 'PricingInfo'
        verbose_name_plural = 'PricingInfos'

class Pricing(BaseField):
    icon = models.CharField( max_length=250)
    name = models.CharField( max_length=250)
    prix = models.IntegerField()
    color = models.BooleanField(default=False)
    periode = models.CharField( max_length=250)
    optionPricing = models.ManyToManyField("service.OptionPricing", verbose_name=("optionPricing"))

    
    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'

    def __str__(self):
        return self.name


class OptionPricing(BaseField):
    
    name = models.CharField( max_length=250)

    
    class Meta:
        verbose_name = 'OptionPricing'
        verbose_name_plural = 'OptionPricings'

    def __str__(self):
        return self.name


class Work(BaseField):
    
    titre = models.CharField( max_length=250)
    image = models.FileField(upload_to='images')
    description = models.TextField()
    image2 = models.FileField(upload_to='images')
    description2 = models.TextField()
    categorie = models.ForeignKey("service.CategorieWork", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.titre



class CategorieWork(BaseField):
    
    nom = models.CharField( max_length=250)
    
    class Meta:
        verbose_name = 'CategorieWork'
        verbose_name_plural = 'CategorieWorks'

    def __str__(self):
        return self.nom

class ImageWork(BaseField):
    
    image = models.FileField(upload_to='images')
    nom = models.CharField( max_length=250)
    work = models.ForeignKey("service.Work", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'ImageWork'
        verbose_name_plural = 'ImageWorks'

    def __str__(self):
        return self.nom

# Create your models here.
