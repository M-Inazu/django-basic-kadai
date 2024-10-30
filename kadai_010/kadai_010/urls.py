"""kadai_010 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    #　関数viewの場合　path(URL, 関数, name=URLの名前)
    path('admin/', admin.site.urls),
    # クラスviewの場合　path(URL, クラス.as_view(), name=URLの名前)
    path('', views.TopView.as_view(), name="top"),

    # 「http://127.0.0.1:8000/crud/」のURLにアクセスできるように設定します。
    path('crud/', views.ProductListView.as_view(), name="list"),

    # 新規作成画面にアクセスした場合のルーティングを設定　ProductCreateViewsクラスを実行するように指定
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),

    # 先ほど定義したProductUpdateFormクラスを実行するように指定する
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),

    # 削除画面にアクセスした場合のルーティングを設定。先ほど定義したProductDeleteFormクラスを実行するように指定
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),

    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),

]