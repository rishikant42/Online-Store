from django_filters import (
    CharFilter,  rest_framework,
)

from store.models import SubCategory


class SubCategoryFilter(rest_framework.FilterSet):
    category_name = CharFilter(
        field_name='category__name',
        lookup_expr='exact',
    )
    category_name__contains = CharFilter(
        field_name='category__name',
        lookup_expr='contains',
    )
    category_name__icontains = CharFilter(
        field_name='category__name',
        lookup_expr='icontains',
    )

    class Meta:
        model = SubCategory
        fields = {
            'uid': ['exact'],
            'name': ['exact', 'contains', 'icontains'],
        }
