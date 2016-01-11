from django.contrib import admin

# Register your models here.
from .models import Videos
from django.contrib.auth.models import User


class VideoInline(admin.StackedInline):
    model = Videos
    extra = 5


class UserAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Videos)
