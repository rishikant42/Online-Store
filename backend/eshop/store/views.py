from rest_framework import generics

from store.models import Category
from store.serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by(
        '-id',
    )
