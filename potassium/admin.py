from django.contrib import admin

from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    model = GalleryImage
    search_fields = ('title', 'description',)
    list_display = ('title', 'description', 'created',)
    readonly_fields = ('created', 'updated',)
