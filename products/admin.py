# vim:fileencoding=utf-8
from products.models import Trader, Region, Category, Images, Product
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from sorl.thumbnail import ImageField
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail.admin.current import AdminImageWidget
from django.core.cache import cache


class AdminInlineImage(AdminImageMixin, admin.TabularInline):
    model = Images
    extra = 2


class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    list_display = ['name', 'category', 'active', 'sort', 'unit_price', 'trader']
    list_filter = ['trader', 'category', 'active']
    list_editable = ['active', 'sort']
    inlines = [AdminInlineImage]


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    formfield_overrides = {
        ImageField: {'widget': AdminImageWidget}
    }


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    formfield_overrides = {
        ImageField: {'widget': AdminImageWidget}
    }


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Trader, SlugAdmin)
admin.site.register(Region, SlugAdmin)