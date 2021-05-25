from django.db import models


class BaseField(models.Model):
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    
    
    class Meta:
        abstract = True



class Banner(BaseField):
    tilte = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.tilte



class ImageBanner(BaseField):
    image = models.FileField(upload_to='images')
    
    class Meta:
        verbose_name = 'ImageBanner'
        verbose_name_plural = 'ImageBanners'



class Team(BaseField):
    name = models.CharField(max_length=200)
    proffession =  models.CharField(max_length=200)
    image = models.FileField(upload_to='images')
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name



class Partner(BaseField):
    icon = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.icon


class AboutInfo(BaseField):
    image = models.FileField(upload_to='images')
    descriptionabout = models.TextField()
    descriptionteam = models.TextField()
    descriptionstat = models.TextField()
    descriptionnewsletters = models.TextField()
    soutitre_image =models.FileField(upload_to='images')
    soutitre_titre = models.CharField(max_length=250)
    option = models.ManyToManyField("siteweb.OptionAbout", verbose_name=("OptionAbout"),null = True)
    
    
    class Meta:
        verbose_name = 'AboutInfo'
        verbose_name_plural = 'AboutInfos'


class Statistique(BaseField):
    name = models.CharField(max_length=250)
    pourcentage = models.IntegerField()
    
    class Meta:
        verbose_name = 'Statistique'
        verbose_name_plural = 'Statistiques'

    def __str__(self):
        return self.name


class OptionAbout(BaseField):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    description = models.TextField()
    
    
    class Meta:
        verbose_name = 'OptionAbout'
        verbose_name_plural = 'OptionAbouts'

    def __str__(self):
        return self.name


class SiteWeb(BaseField):
    icon_logo = models.CharField(max_length=250)
    titre_logo = models.CharField(max_length=250)
    titre_service = models.CharField(max_length=250)
    description = models.TextField()
    icon_service = models.CharField(max_length=250)
    description_footer = models.TextField()
    copyright = models.CharField(max_length=250)
    
    
    
    class Meta:
        verbose_name = 'SiteWeb'
        verbose_name_plural = 'SiteWebs'


# Create your models here.
