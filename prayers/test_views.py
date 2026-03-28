from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase

from prayers.factories import PrayerFactory
from prayers.models import Prayer

factory = APIRequestFactory()
client = APIClient()
request = factory.get("/prayers/")


class TestPrayerBulkGet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.prayer1 = PrayerFactory.create()
        cls.prayer2 = PrayerFactory.create()
        cls.prayer3 = PrayerFactory.create()
        cls.prayer1.category = "Harmony"
        cls.prayer2.category = "Healing"
        cls.prayer3.category = "Hope"
        cls.prayer1.save()
        cls.prayer2.save()
        cls.prayer3.save()

    @classmethod
    def tearDownTestData(cls):
        Prayer.objects.all().delete()

    def test_prayer_bulk_get_returns_correct_number(self):
        response = client.get("/prayers/")
        self.assertEqual(len(response.data[ "prayers" ]), 3)

    def test_prayer_bulk_get_returns_correct_data(self):
        response = client.get("/prayers/")
        self.assertEqual(response.data[ "prayers" ][ 0 ][ "category" ], self.prayer1.category)
        self.assertEqual(response.data[ "prayers" ][ 1 ][ "category" ], self.prayer2.category)
        self.assertEqual(response.data[ "prayers" ][ 2 ][ "category" ], self.prayer3.category)
