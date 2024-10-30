from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy



 # Create your views here.
class TopView(TemplateView):
     template_name = "top.html"

# データの一覧を表示するためのviewを追加する Listviewクラスを継承
class ProductListView(ListView):
     model = Product
   

     #　ページネーションの追加　複数のページに分けて表示が可能になる　class変数paginate_byで1ページに表示する数を指定する。
     # ページネーションはpage_obiという名前のページオブジェクトで管理している。
     paginate_by = 3

# 新規作成
class ProductCreateView(CreateView):
     model = Product
     # 新規作成時にユーザーが入力するフィールドを指定する※ここでは全てのフィールドを指定
     fields = '__all__'

# 商品を編集するためのViewを追加　編集に特化したUpdateViewクラスを利用すると便利
class ProductUpdateView(UpdateView):
     model = Product
     fields = '__all__'
     
     # デフォルトのTemplateファイル名が新規作成フォームと同じ「product_form.html」になるため、
     # template_name_suffixで編集用のTemplateファイル名を指定する
     # Templateファイル名は「product_update_form.html」になる
     template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
     model = Product
     success_url = reverse_lazy('list')

class ProductDetailView(DetailView):
     model = Product
     fields = '__all__'

     template_name_suffix = '_detail'
