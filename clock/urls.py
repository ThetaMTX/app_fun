from django.urls import path
from django.views.generic import RedirectView

import clock
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/clock/')),
    path('clock/', views.clock, name='clock'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)