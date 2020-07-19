import uuid

from django.db import models


class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(
        max_length=255, unique=True, null=False, blank=False
    )

    class Meta:
        db_table = 'category'


class SubCategory(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategory'
        unique_together = (
            ('name', 'category'),
        )


class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'
        unique_together = (
            ('name', 'subcategory'),
        )
