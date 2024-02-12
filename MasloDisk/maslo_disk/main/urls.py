from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('pricing', views.pricing, name='pricing'),
    path('add', views.add, name='add'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='document-details'),
    path('delete/<int:id>', views.deleteDocument, name='delete'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)