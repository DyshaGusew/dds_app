from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from main.views import (
    DDSRecordViewSet,
    StatusViewSet,
    TypeViewSet,
    CategoryViewSet,
    SubCategoryViewSet
)

# Роутер для автоматической генерации URL API
router = DefaultRouter()
router.register(r'ddsrecords', DDSRecordViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'types', TypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)), # Подключение маршрутов API
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('admin:main_ddsrecord_changelist'))),
]
