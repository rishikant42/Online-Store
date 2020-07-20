from django.urls import reverse

from eshop.test_helper import EshopTestCaseBase
from store.models import (
    Category, SubCategory, Product,
)


class StoreTestCaseBase(EshopTestCaseBase):
    def create_category(self, name=None):
        if name is None:
            name = self.create_random_text()

        return Category.objects.create(
            name=name,
        )

    def create_subcategory(self, name=None, category=None):
        if name is None:
            name = self.create_random_text()

        if category is None:
            category = self.create_category()

        return SubCategory.objects.create(
            name=name,
            category=category,
        )

    def create_product(self, name=None, subcategory=None):
        if name is None:
            name = self.create_random_text()

        if subcategory is None:
            subcategory = self.create_subcategory()

        return Product.objects.create(
            name=name,
            subcategory=subcategory,
        )

    def create_bulk_category(self):
        for i in range(10):
            self.create_category()
        return None

    def create_bulk_subcategory(self):
        for i in range(10):
            self.create_subcategory()
        return None

    def create_bulk_product(self):
        for i in range(10):
            self.create_product()
        return None

    def assert_category_list_response(self, results):
        for result in results:
            category = Category.objects.get(
                uid=result.get('uid')
            )
            self.assertEqual(
                result.get('name'),
                category.name
            )
        return None

    def assert_subcategory_list_response(self, results):
        for result in results:
            subcategory = SubCategory.objects.get(
                uid=result.get('uid')
            )
            self.assertEqual(
                result.get('name'),
                subcategory.name
            )
            self.assertEqual(
                result.get('category').get('uid'),
                str(subcategory.category.uid)
            )
            self.assertEqual(
                result.get('category').get('name'),
                subcategory.category.name
            )
        return None

    def assert_product_list_response(self, results):
        for result in results:
            product = Product.objects.get(
                uid=result.get('uid')
            )
            self.assertEqual(
                result.get('name'),
                product.name
            )
            self.assertEqual(
                result.get('subcategory').get('uid'),
                str(product.subcategory.uid)
            )
            self.assertEqual(
                result.get('subcategory').get('name'),
                product.subcategory.name
            )
            self.assertEqual(
                result.get('subcategory').get('category').get('uid'),
                str(product.subcategory.category.uid)
            )
            self.assertEqual(
                result.get('subcategory').get('category').get('name'),
                product.subcategory.category.name
            )
        return None

    def setUp(self):
        super().setUp()
        self.create_bulk_product()


class CategoryListTestCase(StoreTestCaseBase):
    def setUp(self):
        super().setUp()
        self.url = reverse('store:category-list')

    def test_get_category_list(self):
        response = self.client.get(
            self.url,
        )
        expected_count = Category.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), expected_count)
        self.assert_category_list_response(
            response.data.get('results')
        )

    def test_post_without_required_params(self):
        # case-1: missing name

        response = self.client.post(
            self.url,
            {
                # "name": self.create_random_text(),
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.get('name')[0],
            'This field is required.'
        )

    def test_post_unique_constrain_fail(self):
        category = self.create_category()

        # name already exist
        response = self.client.post(
            self.url,
            {
                "name": category.name,
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(response.data.get('name')[0]),
            'category with this name already exists.'
        )

    def test_post_category(self):
        name = self.create_random_text()
        response = self.client.post(
            self.url,
            {
                "name": name,
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data.get('name'),
            name
        )
        self.assert_category_list_response(
            [response.data]
        )


class SubCategoryListTestCase(StoreTestCaseBase):
    def setUp(self):
        super().setUp()
        self.url = reverse('store:subcategory-list')

    def test_get_subcategory_list(self):
        response = self.client.get(
            self.url,
        )
        expected_count = SubCategory.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), expected_count)
        self.assert_subcategory_list_response(
            response.data.get('results')
        )

    def test_filter_uid(self):
        subcategory = self.create_subcategory()
        uid = str(subcategory.uid)
        response = self.client.get(
            self.url,
            {'uid': uid},
        )
        expected_count = SubCategory.objects.filter(
            uid=uid
        ).count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), expected_count)
        self.assert_subcategory_list_response(
            response.data.get('results')
        )

    def test_filter_name(self):
        subcategory = self.create_subcategory()
        name = subcategory.name
        response = self.client.get(
            self.url,
            {'name': name},
        )
        expected_count = SubCategory.objects.filter(
            name=name
        ).count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), expected_count)
        self.assert_subcategory_list_response(
            response.data.get('results')
        )

    def test_filter_category_uid(self):
        subcategory = self.create_subcategory()
        category_uid = str(subcategory.category.uid)
        response = self.client.get(
            self.url,
            {'category_uid': category_uid},
        )
        expected_count = SubCategory.objects.filter(
            category__uid=category_uid
        ).count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), expected_count)
        self.assert_subcategory_list_response(
            response.data.get('results')
        )

    def test_filter_category_name(self):
        subcategory = self.create_subcategory()
        category_name = subcategory.category.name
        response = self.client.get(
            self.url,
            {'category_name': category_name},
        )
        expected_count = SubCategory.objects.filter(
            category__name=category_name
        ).count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), expected_count)
        self.assert_subcategory_list_response(
            response.data.get('results')
        )

    def test_post_without_required_params(self):
        category = self.create_category()

        # case-1: missing name
        response = self.client.post(
            self.url,
            {
                # "name": self.create_random_text(),
                "category_uid": str(category.uid)
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.get('name')[0],
            'This field is required.'
        )

        # case-2: missing category_uid
        response = self.client.post(
            self.url,
            {
                "name": self.create_random_text(),
                # "category_uid": str(category.uid)
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.get('category_uid')[0],
            'This field is required.'
        )

    def test_post_invalid_data(self):
        # case-1: category_uid does not exist
        category_uid = self.create_random_uid()
        response = self.client.post(
            self.url,
            {
                "name": self.create_random_text(),
                "category_uid": category_uid
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(response.data.get('category_uid')[0]),
            f'Object with uid={category_uid} does not exist.'
        )

    def test_post_unique_constrain_fail(self):
        subcategory = self.create_subcategory()

        response = self.client.post(
            self.url,
            {
                "name": subcategory.name,
                "category_uid": str(subcategory.category.uid)
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(response.data.get('unique_together')[0]),
            "The combination of name & category_uid must be unique."
        )

    def test_post_subcategory(self):
        name = self.create_random_text()
        category = self.create_category()

        response = self.client.post(
            self.url,
            {
                "name": name,
                "category_uid": str(category.uid),
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data.get('name'),
            name
        )
        self.assert_subcategory_list_response(
            [response.data]
        )


class ProductListTestCase(StoreTestCaseBase):
    def setUp(self):
        super().setUp()
        self.url = reverse('store:product-list')

    def test_get_product_list(self):
        response = self.client.get(
            self.url,
        )
        expected_count = Product.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('count'), expected_count)
        self.assert_product_list_response(
            response.data.get('results')
        )

    def test_post_without_required_params(self):
        subcategory = self.create_subcategory()

        # case-1: missing name
        response = self.client.post(
            self.url,
            {
                # "name": self.create_random_text(),
                "subcategory_uid": str(subcategory.uid)
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.get('name')[0],
            'This field is required.'
        )

        # case-2: missing subcategory_uid
        response = self.client.post(
            self.url,
            {
                "name": self.create_random_text(),
                # "subcategory_uid": str(subcategory.uid)
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.get('subcategory_uid')[0],
            'This field is required.'
        )

    def test_post_invalid_data(self):
        # case-1: subcategory_uid does not exist
        subcategory_uid = self.create_random_uid()
        response = self.client.post(
            self.url,
            {
                "name": self.create_random_text(),
                "subcategory_uid": subcategory_uid
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(response.data.get('subcategory_uid')[0]),
            f'Object with uid={subcategory_uid} does not exist.'
        )

    def test_post_unique_constrain_fail(self):
        product = self.create_product()
        response = self.client.post(
            self.url,
            {
                "name": product.name,
                "subcategory_uid": str(product.subcategory.uid)
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(response.data.get('unique_together')[0]),
            "The combination of name & subcategory_uid must be unique."
        )

    def test_post_product(self):
        name = self.create_random_text()
        subcategory = self.create_subcategory()

        response = self.client.post(
            self.url,
            {
                "name": name,
                "subcategory_uid": str(subcategory.uid),
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data.get('name'),
            name
        )
        self.assert_product_list_response(
            [response.data]
        )
