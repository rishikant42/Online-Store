from rest_framework import serializers

from store.models import (
    Category, SubCategory, Product,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'uid', 'name',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True,
    )
    category_uid = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='uid',
        write_only=True,
        required=True,
    )

    def create(self, validated_data):
        category = validated_data.pop('category_uid')

        validated_data['category'] = category

        return super().create(validated_data)

    class Meta:
        model = SubCategory
        fields = (
            'uid', 'name', 'category', 'category_uid',
        )


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(
        read_only=True,
    )
    subcategory_uid = serializers.SlugRelatedField(
        queryset=SubCategory.objects.all(),
        slug_field='uid',
        write_only=True,
        required=True,
    )

    def create(self, validated_data):
        subcategory = validated_data.pop('subcategory_uid')

        validated_data['subcategory'] = subcategory

        return super().create(validated_data)

    class Meta:
        model = Product
        fields = (
            'uid', 'name', 'subcategory', 'subcategory_uid',
        )
