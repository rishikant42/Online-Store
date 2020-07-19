from django.urls import path

from store import views

app_name = 'store'
urlpatterns = [
    path('categories/',
         views.CategoryList.as_view(),
         name='category-list'),
    path('subcategories/',
         views.SubCategoryList.as_view(),
         name='subcategory-list'),
]
