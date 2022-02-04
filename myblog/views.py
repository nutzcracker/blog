from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Dossier
from django.core.paginator import Paginator
from .forms import SigUpForm

class MainView(View):
    def get(self, request, *args, **kwargs):
        dossiers = Dossier.objects.all()
        paginator = Paginator(dossiers, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,'myblog/home.html', context={'page_obj': page_obj}
        )

class DossierDetail(View):
    def get(self, request, dossier_id, *args, **kwargs):
        dossier = get_object_or_404(Dossier, id=dossier_id)
        return render(request, 'myblog/dossier_detail.html', context={
            'dossier': dossier
    })

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })