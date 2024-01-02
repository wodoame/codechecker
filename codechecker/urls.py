from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check, name='check'),
    path('export_records/', views.export_records, name='export_records'),
    path('setup/', views.SetupEvent.as_view(), name='setup'),
    path('event/<slug:slug>', views.ViewEvent.as_view(), name='event'),
    path('attendance/<int:id>', views.AttendanceList.as_view(), name='attendance'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
]
