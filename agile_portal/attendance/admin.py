from django.contrib import admin
from .models import GeoPolygon, AttendReport, eDetail

# Register your models here.
admin.site.register(GeoPolygon)
admin.site.register(AttendReport)
admin.site.register(eDetail)