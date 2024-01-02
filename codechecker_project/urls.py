from django.contrib import admin
from django.urls import path, include
from codechecker.views import check
from codechecker.views import export_records
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    # Define URL patterns for your views
    path('', check, name='home'),  # This makes the 'check' view your home page
    path('export-records/', export_records, name='export_records'),

    # Include URL patterns from your 'codechecker' app
    path('app/', include('codechecker.urls')),

    # Additional project-level URL patterns can be defined here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
