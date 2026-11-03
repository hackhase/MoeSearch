from django.contrib import admin
from django.urls import path
from .views import SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', SearchView.as_view(), name='search'), # 🎯 极简 API
]