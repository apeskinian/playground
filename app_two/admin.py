from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Watch

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('make','collection','model',)}
