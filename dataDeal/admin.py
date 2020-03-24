from django.contrib import admin
from .models import picDataSet,picData
# Register your models here.

@admin.register(picDataSet)
class PicDataSetAdmin(admin.ModelAdmin):
    list_display = ("dataName","create_time","user")


@admin.register(picData)
class PicDataAdmin(admin.ModelAdmin):
    list_display = ("typeData","wordData","log","lat")

