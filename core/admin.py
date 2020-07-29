from django.contrib.admin import ModelAdmin
from my_admin.admin import admin_site
from django.contrib import admin
from core.models import *

@admin.register(Category, site=admin_site)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(Book, site=admin_site)
class BookAdmin(ModelAdmin):
    search_fields = ('title',)

@admin.register(CreditCard, site=admin_site)
class CreditCardAdmin(ModelAdmin):
    search_fields = ('number',)
