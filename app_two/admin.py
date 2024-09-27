from django.contrib import admin
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.utils import get_attachment_model 
from .models import Watch

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('make', 'collection', 'model', 'owner')
    list_filter = ('owner','status')
    prepopulated_fields = {'slug':('make','collection','model',)}

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)
admin.site.unregister(Site)
admin.site.unregister(get_attachment_model())