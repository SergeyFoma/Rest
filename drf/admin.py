from django.contrib import admin
from drf.models import Category, Women

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name',]

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display=['id','title','content','time_create','time_update','is_published','cat']

# Register your models here.
