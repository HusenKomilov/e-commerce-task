from django.contrib import admin
from django.utils.safestring import mark_safe
from products import models


class GalleryAdmin(admin.TabularInline):
    fk_name = "product"
    model = models.Gallery
    extra = 1


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    prepopulated_fields = {
        "slug": ("title",)
    }


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "quantity", "get_photo")
    inlines = [GalleryAdmin]
    prepopulated_fields = {
        "slug": ("title",)
    }

    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f"<img src='{obj.images.all()[0].image.url}' width='75'>")
            except:
                return "-"
        else:
            return "-"


admin.site.register(models.Gallery)
admin.site.register(models.Review)