from django.db.utils import IntegrityError

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

        try:
            instance = super().create(validated_data)
        except IntegrityError as e:
            err_msg = 'The combination of name & category_uid must be unique.'
            if 'UNIQUE constraint failed' in str(e):
                raise serializers.ValidationError({
                    'unique_together': [err_msg]
                })
            raise
        return instance

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

        try:
            instance = super().create(validated_data)
        except IntegrityError as e:
            err = 'The combination of name & subcategory_uid must be unique.'
            if 'UNIQUE constraint failed' in str(e):
                raise serializers.ValidationError({
                    'unique_together': [err]
                })
            raise
        return instance

    class Meta:
        model = Product
        fields = (
            'uid', 'name', 'subcategory', 'subcategory_uid',
        )
