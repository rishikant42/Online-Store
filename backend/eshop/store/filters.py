from django_filters import (
    CharFilter,  rest_framework,
)

from store.models import SubCategory


class SubCategoryFilter(rest_framework.FilterSet):
    category_name = CharFilter(
        field_name='category__name',
        lookup_expr='exact',
    )
    category_uid = CharFilter(
        field_name='category__uid',
        lookup_expr='exact',
    )

    class Meta:
        model = SubCategory
        fields = {
            'uid': ['exact'],
            'name': ['exact'],
        }
