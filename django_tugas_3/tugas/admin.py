from django.contrib import admin
from .models import Tugas

class TugasAdmin(admin.ModelAdmin):
    list_display = ('username', 'name')

# Register your models here.

admin.site.register(Tugas, TugasAdmin)

