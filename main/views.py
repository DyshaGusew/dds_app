from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from main.models import Status, Type, Category, SubCategory, DDSRecord
from main.serializers import (
    StatusSerializer,
    TypeSerializer,
    CategorySerializer,
    SubCategorySerializer,
    DDSRecordSerializer
)

class StatusViewSet(viewsets.ModelViewSet):
    """
    API для управления статусами
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class TypeViewSet(viewsets.ModelViewSet):
    """
    API для управления типами операций
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API для управления категориями
    """
    queryset = Category.objects.select_related('type')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type']

class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API для управления подкатегориями
    """
    queryset = SubCategory.objects.select_related('category', 'category__type')
    serializer_class = SubCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category']

class DDSRecordViewSet(viewsets.ModelViewSet):
    """
    API для управления записями ДДС
    """
    queryset = DDSRecord.objects.select_related('status', 'type', 'category', 'sub_category')
    serializer_class = DDSRecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_created', 'status', 'type', 'category', 'sub_category']