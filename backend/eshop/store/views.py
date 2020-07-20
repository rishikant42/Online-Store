from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from store.models import (
    Category, SubCategory, Product,
)
from store.serializers import (
    CategorySerializer, SubCategorySerializer, ProductSerializer,
)
from store.filters import SubCategoryFilter


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by(
        'name',
    )


class SubCategoryList(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = SubCategoryFilter
    queryset = SubCategory.objects.select_related(
        'category',
    ).order_by(
        'name', 'category__name',
    )


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related(
        'subcategory',
    ).order_by(
       'subcategory__category__name', 'subcategory__name', 'name',
    )
