from django.contrib import admin
from .models import Status
from .forms import StatusModelForm

# Register your models here.
class StatusModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'image']
    form = StatusModelForm

admin.site.register(Status, StatusModelAdmin)