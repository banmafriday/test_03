from django.contrib import admin
from django.urls import path
from app_personal import views as personal_views
from app_manage import views as manage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', personal_views.hello),

    # 账户管理
    path('', personal_views.login),
    path('login/', personal_views.login),
    path('logout/', personal_views.logout),

    # 项目管理
    path('mange/', manage_view.mange)

]
