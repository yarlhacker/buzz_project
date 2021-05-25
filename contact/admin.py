from django.contrib import admin
from . import models 

@admin.register(models.InfoContact)
class InfoContactAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('tilte', 'create_at', 'update_at', 'status')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name', 'create_at', 'update_at', 'status')

@admin.register(models.TeamContact)
class TeamContactAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('personne', 'create_at', 'update_at', 'status')


@admin.register(models.Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('email', 'create_at', 'update_at', 'status')

# Register your models here.

