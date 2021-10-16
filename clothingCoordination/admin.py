from django.contrib import admin

from .models import coordinateInfo

# Register your models here.
class CoordinateInfoAdmin(admin.ModelAdmin):
    list_display = ('coordinate_name', 'user_id', 'created_at')

admin.site.register(coordinateInfo, CoordinateInfoAdmin)
