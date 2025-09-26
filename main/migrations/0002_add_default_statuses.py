from django.db import migrations

def create_initial_data(apps, schema_editor):
    """
    Создает начальные записи для моделей Status, Type, Category, SubCategory.
    """
    Status = apps.get_model('main', 'Status')
    Type = apps.get_model('main', 'Type')
    Category = apps.get_model('main', 'Category')
    SubCategory = apps.get_model('main', 'SubCategory')

    # Статусы
    Status.objects.create(name="Бизнес")
    Status.objects.create(name="Личное")
    Status.objects.create(name="Налог")

    # Типы
    type_income = Type.objects.create(name="Пополнение")
    type_expense = Type.objects.create(name="Списание")

    # Категории
    cat_infra = Category.objects.create(name="Инфраструктура", type=type_expense)
    cat_marketing = Category.objects.create(name="Маркетинг", type=type_expense)

    # Подкатегории
    SubCategory.objects.create(name="VPS", category=cat_infra)
    SubCategory.objects.create(name="Proxy", category=cat_infra)
    SubCategory.objects.create(name="Farpost", category=cat_marketing)
    SubCategory.objects.create(name="Avito", category=cat_marketing)

class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
