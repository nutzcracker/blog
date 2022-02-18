from django.urls import path
from .views import ( MainView, DossierDetail, SignUpView, SignInView, FeedBackView, SuccessView,
SearchResultsView, TagView )
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<int:dossier_id>/', DossierDetail.as_view(), name='dossier_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tag/<dossier_id>/', TagView.as_view(), name="tag"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)