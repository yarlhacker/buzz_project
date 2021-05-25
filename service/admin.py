from django.contrib import admin
from . import models 


@admin.register(models.CategorieService)
class CategorieServiceAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name', 'create_at', 'update_at', 'status')


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('titre', 'create_at', 'update_at', 'status')


@admin.register(models.PricingInfo)
class PricingInfoAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('create_at', 'update_at', 'status')



@admin.register(models.Pricing)
class PricingAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name','create_at', 'update_at', 'status')

@admin.register(models.OptionPricing)
class OptionPricingAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name','create_at', 'update_at', 'status')

@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('titre','create_at', 'update_at', 'status')


@admin.register(models.CategorieWork)
class CategorieWorkAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('nom','create_at', 'update_at', 'status')


@admin.register(models.ImageWork)
class ImageWorkAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('nom','create_at', 'update_at', 'status')
# Register your models here.
