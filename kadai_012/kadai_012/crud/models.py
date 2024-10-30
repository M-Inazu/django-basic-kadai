# 「商品名」と「金額」のフィールドを持ったModelを追加
# フィールドはDjangoに用意されているデータの入れ物
# Modelはmodels.pyで定義する　
from django.db import models
from django.urls import reverse


# カテゴリモデルの追加
class Category(models.Model):
     name = models.CharField(max_length=200)
 
     def __str__(self):
         return self.name

# Create your models here.
# class Product（Modelクラス名）(models.Model):
# neme(フィールド) = models.CharField(フィールドの型)(max_length=200)（フィールドオプション）
# モデルに追加 ForeignKeyフィールドが保持する参照先のオブジェクトと関連するすべてのデータが削除されます。on_delete属性には、以下の値を指定できます。
# CASCADE：関連付けられたオブジェクトが削除された場合、これに関連するすべてのオブジェクトも削除されます。
# 商品Modelに画像フィールドを追加します。
class Product(models.Model):
     name = models.CharField(max_length=200)
     price = models.PositiveIntegerField()
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     img = models.ImageField(blank=True, default='noImage.png')
     explain = models.TextField(blank=True, null=True)

     # Model内に「str(self)」を定義すると、一覧画面で表示される名称を変更できます。ここでは商品名を返します
     def __str__(self):
         return self.name
     
     # 新規作成・編集完了時のリダイレクト先
     def get_absolute_url(self):
          return reverse('list')