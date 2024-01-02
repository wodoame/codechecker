from django.contrib import admin
from .models import Record, Event, AttendanceRecord

admin.site.register(Record)
admin.site.register(Event)
admin.site.register(AttendanceRecord)