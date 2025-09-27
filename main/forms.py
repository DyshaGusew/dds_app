from django import forms
from main.models import DDSRecord

class DDSRecordAdminForm(forms.ModelForm):
    """
    Форма для админ-панели DDSRecord с валидацией зависимостей.
    """
    class Meta:
        model = DDSRecord
        fields = '__all__'

    def clean(self):
        """
        Проверяет соответствие категории типу и подкатегории категории.
        Вызывает ValidationError при несоответствии.
        """
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        type = cleaned_data.get('type')
        sub_category = cleaned_data.get('sub_category')

        if category and type and category.type != type:
            raise forms.ValidationError(
                f"Категория '{category}' не соответствует типу '{type}'. Выберите категорию, связанную с типом '{type}'."
            )
        
        if sub_category and category and sub_category.category != category:
            raise forms.ValidationError(
                f"Подкатегория '{sub_category}' не соответствует категории '{category}'. Выберите подкатегорию, связанную с категорией '{category}'."
            )