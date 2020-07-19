from rest_framework import generics

from store.models import (
    Category, SubCategory,
)
from store.serializers import (
    CategorySerializer, SubCategorySerializer,
)


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by(
        '-id',
    )


class SubCategoryList(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.select_related(
        'category',
    ).order_by(
        '-id',
    )
