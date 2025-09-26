from django.contrib import admin
from .forms import DDSRecordAdminForm
from main.models import Category, DDSRecord, Status, SubCategory, Type
from django.contrib.auth.models import User, Group

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
        """
        Отображение типа категории в списке.
        """
        return obj.category.type
    category_type.short_description = 'Тип категории'


@admin.register(DDSRecord)
class DDSRecordAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели DDSRecord.
    """
    form = DDSRecordAdminForm  # Используем кастомную форму с валидацией
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
        'date_created',
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
    list_per_page = 20

    def comment_short(self, obj):
        """
        Сокращенное отображение комментария в списке (до 50 символов).
        """
        return obj.comment[:50] + '...' if obj.comment and len(obj.comment) > 50 else obj.comment
    comment_short.short_description = 'Комментарий'