from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Dossier, Comment
from django.core.paginator import Paginator
from .forms import SigUpForm, SignInForm, FeedBackForm, CommentForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from taggit.models import Tag


class MainView(View):
    def get(self, request, *args, **kwargs):
        dossiers = Dossier.objects.all()
        paginator = Paginator(dossiers, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,'myblog/home.html', context={'page_obj': page_obj}
        )

class DossierDetail(View):
    def get(self, request, dossier_id, *args, **kwargs):
        dossier = get_object_or_404(Dossier, id=dossier_id)
        common_tags = Dossier.tag.most_common()
        last_dossiers = Dossier.objects.all().order_by('-id')[:3]
        comment_form = CommentForm()
        return render(request, 'myblog/dossier_detail.html', context={
            'dossier': dossier,
            'common_tags' : common_tags,
            'last_dossiers' : last_dossiers,
            'comment_form': comment_form,
    })

    def post(self, request, dossier_id, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            dossier = get_object_or_404(Dossier, id=dossier_id)
            comment = Comment.objects.create(dossier=dossier, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'myblog/post_detail.html', context={
            'comment_form': comment_form
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

class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'myblog/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signin.html', context={
            'form': form,
        })

class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'myblog/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['amromashov@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'myblog/contact.html', context={
            'form': form,
        })

class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/success.html', context={
            'title': 'Спасибо'
        })

class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = Dossier.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })

class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Dossier.objects.filter(tag=tag)
        common_tags = Dossier.tag.most_common()
        return render(request, 'myblog/tag.html', context={
            'title': f'#ТЕГ {tag}',
            'posts': posts,
            'common_tags': common_tags
        })