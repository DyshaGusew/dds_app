from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Status(models.Model):
    """
    Модель для хранения статусов записей ДДС
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Название статуса")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ['name']


class Type(models.Model):
    """
    Модель для хранения типов операций ДДС
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Название типа")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
        ordering = ['name']


class Category(models.Model):
    """
    Модель для хранения категорий операций ДДС
    """
    name = models.CharField(max_length=100, verbose_name="Название категории")

    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name="Тип операции"
    )

    class Meta:
        unique_together = ['name', 'type'] # Уникальность комбинации названия категории и типа
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.type.name})"
        


class SubCategory(models.Model):
    """
    Модель для хранения подкатегорий операций ДДС \n
    Подкатегории привязаны к категориям (Category)
    """
    name = models.CharField(max_length=100, verbose_name="Название подкатегории")

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name="Категория"
    )


    class Meta:
        unique_together = ['name', 'category'] # Уникальность комбинации названия подкатегории и категории
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class DDSRecord(models.Model):
    """
    Модель для хранения записей о движении денежных средств (ДДС).
    """
    date_created = models.DateField(
        default=timezone.now,
        editable=True,
        verbose_name="Дата создания"
    )
    # Поле date_created: дата создания записи, по умолчанию текущая дата, редактируема.

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='records',
        verbose_name="Статус"
    )

    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        related_name='records',
        verbose_name="Тип операции"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='records',
        verbose_name="Категория"
    )

    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        related_name='records',
        verbose_name="Подкатегория"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Сумма (руб)"
    )
    # Поле amount: сумма в рублях, максимум 12 цифр, 2 знака после запятой, минимум 0.01.

    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    def __str__(self):
        return f"Запись {self.id} - {self.date_created} - {self.amount} руб."

    class Meta:
        verbose_name = "Запись ДДС"
        verbose_name_plural = "Записи ДДС"
        ordering = ['-date_created']
        indexes = [
            models.Index(fields=['date_created']),
            models.Index(fields=['status']),
            models.Index(fields=['type']),
            models.Index(fields=['category']),
            models.Index(fields=['sub_category']),
        ]