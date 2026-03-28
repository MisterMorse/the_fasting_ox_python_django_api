from django.test import TestCase

from prayers.factories import PrayerFactory
from prayers.models import Prayer


class PrayerFactoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.prayer1 = PrayerFactory.create()
        cls.prayer2 = PrayerFactory.create()

    @classmethod
    def tearDownTestData(cls):
        Prayer.objects.all().delete()

    def test_prayer_factory_uses_correct_model(self):
        self.assertIsInstance(self.prayer1, Prayer)

    def test_prayer_factory_creates_prayer_with_category(self):
        self.assertNotEqual(self.prayer1.category, "")

    def test_prayer_factory_creates_prayer_with_unique_category(self):
        self.assertNotEqual(self.prayer1.category, self.prayer2.category)
        
    def test_prayer_factory_creates_prayer_with_name(self):
        self.assertNotEqual(self.prayer1.name, "")

    def test_prayer_factory_creates_prayer_with_unique_name(self):
        self.assertNotEqual(self.prayer1.name, self.prayer2.name)

    def test_prayer_factory_creates_prayer_with_description(self):
        self.assertNotEqual(self.prayer1.description, "")

    def test_prayer_factory_creates_prayer_with_unique_description(self):
        self.assertNotEqual(self.prayer1.description, self.prayer2.description)

    def test_prayer_factory_creates_prayer_with_created_at(self):
        self.assertNotEqual(self.prayer1.created_at, "")

    def test_prayer_factory_creates_prayer_with_unique_created_at(self):
        self.assertNotEqual(self.prayer1.created_at, self.prayer2.created_at)

    def test_prayer_factory_creates_prayer_with_updated_at(self):
        self.assertNotEqual(self.prayer1.updated_at, "")

    def test_prayer_factory_creates_prayer_with_unique_updated_at(self):
        self.assertNotEqual(self.prayer1.updated_at, self.prayer2.updated_at)
