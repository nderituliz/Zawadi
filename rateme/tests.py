from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Lizzie', password='12345678.')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
