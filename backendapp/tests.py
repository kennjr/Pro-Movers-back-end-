import os
from django.test import TestCase

# Create your tests here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

# Create your tests here.
from backendapp.models import RegUser, Mover, Request, Rating, User


class ProfileTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345", email="user@users.com")

        self.test_mover = Mover(user=self.test_user, phone='123456', name="The moving Co.", description="test_loc",
                                location="A gen location")

    # testing instance
    def test_instance(self):
        mover = self.test_mover
        self.assertEqual(self.test_mover, mover)

    # testing save method
    def test_save_mover_method(self):
        original_len = Mover.get_all_movers()
        print(f'original len {len(original_len)}')
        self.test_mover.save_mover()

        new_len = Mover.get_all_movers()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_mover_method(self):
        self.test_mover.save_mover()
        original_len = Mover.objects.all()
        print(f'the categorys are{len(original_len)}')
        Mover.delete_mover(self.test_mover.id)
        new_len = Mover.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_mover_by_id_method(self):
        self.test_mover.save_mover()
        req_result = Mover.get_mover_by_id(self.test_mover.id)
        self.assertTrue(req_result is not None)

    def test_get_mover_by_auth_username(self):
        self.test_mover.save_mover()

        req_result = Mover.get_mover_by_username("theuser")
        self.assertTrue(req_result is not None)

    def test_get_mover_by_user_user_id(self):
        self.test_mover.save_mover()

        req_result = Mover.get_mover_user_by_id(self.test_user.id)
        self.assertTrue(req_result is not None)
