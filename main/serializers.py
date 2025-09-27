from rest_framework import serializers
from main.models import Status, Type, Category, SubCategory, DDSRecord

class StatusSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Status
    """
    class Meta:
        model = Status
        fields = ['id', 'name']

class TypeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Type
    """
    class Meta:
        model = Type
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category
    """
    type = TypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), source='type', write_only=True
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'type_id']

class SubCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели SubCategory
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'category_id']

class DDSRecordSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели DDSRecord
    """
    status = StatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source='status', write_only=True
    )
    type = TypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), source='type', write_only=True
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    sub_category = SubCategorySerializer(read_only=True)
    sub_category_id = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(), source='sub_category', write_only=True
    )

    class Meta:
        model = DDSRecord
        fields = [
            'id',
            'date_created',
            'status',
            'status_id',
            'type',
            'type_id',
            'category',
            'category_id',
            'sub_category',
            'sub_category_id',
            'amount',
            'comment'
        ]

    def validate(self, data):
        """
        Проверяет соответствие категории типу и подкатегории категории
        """
        category = data.get('category')
        type = data.get('type')
        sub_category = data.get('sub_category')

        if category and type and category.type != type:
            raise serializers.ValidationError(
                f"Категория '{category}' не соответствует типу '{type}'."
            )
        if sub_category and category and sub_category.category != category:
            raise serializers.ValidationError(
                f"Подкатегория '{sub_category}' не соответствует категории '{category}'."
            )
        return data
