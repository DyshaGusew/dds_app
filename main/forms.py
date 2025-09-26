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
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        type = cleaned_data.get('type')
        sub_category = cleaned_data.get('sub_category')

        if category and type and category.type != type:
            raise forms.ValidationError("Категория не соответствует выбранному типу.")
        if sub_category and category and sub_category.category != category:
            raise forms.ValidationError("Подкатегория не соответствует выбранной категории.")