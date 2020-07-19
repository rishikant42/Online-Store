import random
import string
import uuid

from django.test import (
    TestCase, Client
)


class EshopTestCaseBase(TestCase):
    def create_random_text(self, length=8):
        return ''.join(random.choices(
            string.ascii_letters + string.digits, k=length))

    def create_random_number(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def create_random_uid(self):
        return str(uuid.uuid4())

    def setUp(self):
        self.client = Client()
