from django.shortcuts import render
from django.views import View
from .models import Dossier

class MainView(View):
    def get(self, request, *args, **kwargs):
        dossiers = Dossier.objects.all()
        return render(request,'myblog/home.html', context={'dossiers': dossiers}
        )
# Create your views here.
