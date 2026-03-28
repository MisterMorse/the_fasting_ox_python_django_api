from django.test import TestCase

from prayers.factories import PrayerFactory
from prayers.models import Prayer


class PrayerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.prayer = PrayerFactory.create()

    @classmethod
    def tearDownTestData(cls):
        Prayer.objects.all().delete()

    def test_prayer_category_name(self):
        category_name = Prayer._meta.get_field("category").verbose_name
        self.assertEqual(category_name, "category")

    def test_prayer_name_name(self):
        name_name = Prayer._meta.get_field("name").verbose_name
        self.assertEqual(name_name, "name")

    def test_prayer_description_name(self):
        description_name = Prayer._meta.get_field("description").verbose_name
        self.assertEqual(description_name, "description")

    def test_prayer_created_at_name(self):
        created_at_name = Prayer._meta.get_field("created_at").verbose_name
        self.assertEqual(created_at_name, "created at")

    def test_prayer_updated_at_name(self):
        updated_at_name = Prayer._meta.get_field("updated_at").verbose_name
        self.assertEqual(updated_at_name, "updated at")

    def test_prayer_category_max_length(self):
        max_length = Prayer._meta.get_field("category").max_length
        self.assertEqual(max_length, 100)

    def test_prayer_name_max_length(self):
        max_length = Prayer._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)

    # I need to put some tests in here so that I can test the time created_at and updated_at
    # are recorded to confirm the parameters; I may put in freezegun, but the architecture
    # changes are beyond what I can do before a commit. Similarly, I need to test the ordering,
    # but it is multiple levels of organization, which is going to take a significant amount
    # of manual labor. I"m going to put an Issue in the GitHub repo.

    def test_prayer_string_method(self):
        expected_object_string = f"{self.prayer.category} -> {self.prayer.name}"
        self.assertEqual(self.prayer.__str__(), expected_object_string)
