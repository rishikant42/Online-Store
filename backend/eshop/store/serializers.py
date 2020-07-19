from rest_framework import serializers

from store.models import (
    Category, SubCategory,
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
        required=False,
    )

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
        required=False,
    )

    class Meta:
        model = SubCategory
        fields = (
            'uid', 'name', 'subcategory', 'subcategory_uid',
        )
