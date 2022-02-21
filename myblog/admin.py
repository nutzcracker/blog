from django.contrib import admin

# Register your models here.
from .models import Dossier, Comment

class DossierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dossier)
admin.site.register(Comment)
