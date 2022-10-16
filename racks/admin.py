from django.contrib import admin


from django.contrib import admin
from .models import django_rack,python_rack,pandas_rack


class djangoadmin(admin.ModelAdmin):
    list_display=['subject','explanation']
admin.site.register(django_rack,djangoadmin)


class pythonadmin(admin.ModelAdmin):
    list_display=['subject','explanation']
admin.site.register(python_rack,pythonadmin)

class pythonpandas(admin.ModelAdmin):
    list_display=['subject','explanation']
admin.site.register(pandas_rack,pythonadmin)

