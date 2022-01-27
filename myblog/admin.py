from django.contrib import admin

# Register your models here.
from .models import Dossier

class DossierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dossier)
