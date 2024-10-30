from django.contrib import admin
from .models import Product
from .models import Product, Category
# 管理画面にimgタグを出力するためにmark_safe関数を使用する
from django.utils.safestring import mark_safe
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'price', 'category','image')
     search_fields = ('name',)
     list_filter = ('category',)

     def image(self, obj):
         return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

# 管理画面のカテゴリーについてクラス設定
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_fields = ('name',)
     
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)