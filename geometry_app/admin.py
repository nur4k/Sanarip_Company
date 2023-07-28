from django.contrib import admin

from geometry_app.models import Region, District, Canton, Contour


admin.site.register((Region, District, Canton, Contour))
