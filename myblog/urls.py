from django.urls import path
from .views import MainView, DossierDetail, SignUpView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<int:dossier_id>/', DossierDetail.as_view(), name='dossier_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)