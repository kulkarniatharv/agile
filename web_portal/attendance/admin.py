from django.contrib import admin
from .models import aReports, GeoLocation, eDetails

# Register your models here.
#@admin.register(aReports)
#@admin.register(GeoLocation)
#@admin.register(eDetails)

admin.site.register(aReports)
admin.site.register(GeoLocation)
admin.site.register(eDetails)

