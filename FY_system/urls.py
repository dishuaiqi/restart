"""FY_system URL Configuration

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
from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    #用户主页
    path('', views.home),
    #用户登录页面
    path('login/', views.login),
    path('logout/', views.logout),

    #向表中添加数据
    path('orm/',views.orm),

    #展示用户列表
    path('user/list/',views.user_list),
    path('user/add/',views.user_add),
    path('user/edit/',views.user_edit),

    path('user/delete/',views.user_delete),
    path('select/date/',views.select_date),

    #展示用户详情
    path('user/xiangqing/', views.user_xiangqing),
    path('xiangqing/add/', views.user_xiangqing_add),
    path('user/xiangqing/edit/', views.user_xiangqing_edit),

    path('user/xiangqing/delete/', views.user_xiangqing_delete),

    #提货展示
    path('tihuo/zhanshi/',views.tihuo_zhanshi),
    path('tihuo/zhanshi/add/',views.tihuo_add),
    path('tihuo/zhanshi/edit/',views.tihuo_edit),

    path('tihuo/zhanshi/delete/',views.tihuo_delete),


    #数据展示
    path('shuju/zhanshi/',views.shuju_zhanshi),
    path('shuju/tu/',views.shuju_tu),

]
