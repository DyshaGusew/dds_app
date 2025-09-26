from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from .forms import DDSRecordAdminForm
from main.models import Category, DDSRecord, Status, SubCategory, Type
from django.contrib.auth.models import User, Group
from rangefilter.filters import DateRangeFilter


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Status.
    """
    list_display = ('name',)  # Отображаемые поля в списке
    search_fields = ('name',)  # Поля для поиска
    list_filter = ('name',)  # Фильтры в админке
    ordering = ('name',) # Сортировка по имени

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Type.
    """
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Category.
    """
    list_display = ('name', 'type')
    search_fields = ('name', 'type__name')
    list_filter = ('type',)
    list_select_related = ('type',)
    ordering = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели SubCategory.
    """
    list_display = ('name', 'category', 'category_type')
    search_fields = ('name', 'category__name', 'category__type__name')
    list_filter = ('category', 'category__type')
    list_select_related = ('category', 'category__type')

    def category_type(self, obj):
        return obj.category.type
    category_type.short_description = 'Тип категории'


@admin.register(DDSRecord)
class DDSRecordAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели DDSRecord.
    """
    form = DDSRecordAdminForm  # Кастомная форма с валидацией
    list_display = (
        'date_created',
        'status',
        'type',
        'category',
        'sub_category',
        'amount',
        'comment_short'
    )
    list_filter = (
        ('date_created', DateRangeFilter),
        'status',
        'type',
        'category',
        'sub_category'
    )
    search_fields = (
        'status__name',
        'type__name',
        'category__name',
        'sub_category__name',
        'comment'
    )
    list_select_related = (
        'status',
        'type',
        'category',
        'sub_category'
    )
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)
    autocomplete_fields = ('status', 'type')
    list_per_page = 20

    def comment_short(self, obj):
        """
        Сокращенное отображение комментария в списке (до 50 символов).
        """
        return obj.comment[:50] + '...' if obj.comment and len(obj.comment) > 50 else obj.comment
    
    comment_short.short_description = 'Комментарий'

    # JavaScript для динамической фильтрации
    class Media:
        js = ('main/js/admin_dynamic_subcategory.js',)

    # URL для получения подкатегорий через AJAX
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_subcategories/', self.admin_site.admin_view(self.get_subcategories), name='get_subcategories'),
        ]
        return custom_urls + urls

    def get_subcategories(self, request):
        """Возвращает список подкатегорий для выбранной категории в формате JSON."""
        category_id = request.GET.get('category_id')
        subcategories = []
        if category_id:
            subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
        return JsonResponse({'subcategories': list(subcategories)})
