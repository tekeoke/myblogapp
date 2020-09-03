from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

# from django.urls import poth
# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path(URLパターン, ビュー関数),...
# ]