from django.contrib import admin
from .models import Cat, Photo

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 9

class CatAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]

admin.site.register(Cat, CatAdmin)