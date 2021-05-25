from django.contrib import admin
from . import models


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('tilte', 'create_at', 'update_at', 'status')

@admin.register(models.ImageBanner)
class ImageBannerAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('create_at', 'update_at', 'status')

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name','create_at', 'update_at', 'status')


@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('create_at', 'update_at', 'status')


@admin.register(models.AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('create_at', 'update_at', 'status')


@admin.register(models.Statistique)
class StatistiqueAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name','create_at', 'update_at', 'status')


@admin.register(models.OptionAbout)
class OptionAboutAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name','create_at', 'update_at', 'status')



@admin.register(models.SiteWeb)
class SiteWebAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('titre_logo','create_at', 'update_at', 'status')

# Register your models here.
