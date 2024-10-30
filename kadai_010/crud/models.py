# 「商品名」と「金額」のフィールドを持ったModelを追加
# フィールドはDjangoに用意されているデータの入れ物
# Modelはmodels.pyで定義する　
from django.db import models
from django.urls import reverse

# Create your models here.
# class Product（Modelクラス名）(models.Model):
# neme(フィールド) = models.CharField(フィールドの型)(max_length=200)（フィールドオプション）
class Product(models.Model):
     name = models.CharField(max_length=200)
     price = models.PositiveIntegerField()

     # Model内に「str(self)」を定義すると、一覧画面で表示される名称を変更できます。ここでは商品名を返します
     def __str__(self):
         return self.name
     
     # 新規作成・編集完了時のリダイレクト先
     def get_absolute_url(self):
          return reverse('list')
