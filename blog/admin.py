from django.contrib import admin
from django.utils.safestring import mark_safe
from blog import models


class PostGallery(admin.TabularInline):
    fk_name = "post"
    model = models.PostGallery
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "get_photo")
    inlines = [PostGallery]

    def get_photo(self, obj):
        if obj.main_photo:
            try:
                return mark_safe(f"<img src='{obj.main_photo.url}' width='75'>")
            except:
                return "-"
        else:
            return "-"

    get_photo.short_description = "Post Image"


admin.site.register(models.PostGallery)
admin.site.register(models.Mail)
admin.site.register(models.Contact)
