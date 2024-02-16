from django.contrib import admin

from goods.models import Category, Product

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
