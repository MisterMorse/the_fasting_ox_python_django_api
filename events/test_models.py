from django.test import TestCase

from events.models import Event
from events.factories import EventFactory

class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.event = EventFactory.create()

    @classmethod
    def tearDownTestData(cls):
        Event.objects.all().delete()

    def test_event_category_name(self):
        category_name = Event._meta.get_field('category').verbose_name
        self.assertEqual(category_name, 'category')

    def test_event_name_name(self):
        name_name = Event._meta.get_field('name').verbose_name
        self.assertEqual(name_name, 'name')

    def test_event_description_name(self):
        description_name = Event._meta.get_field('description').verbose_name
        self.assertEqual(description_name, 'description')

    def test_event_location_name(self):
        location_name = Event._meta.get_field('location').verbose_name
        self.assertEqual(location_name, 'location')

    def test_event_date_name(self):
        date_name = Event._meta.get_field('date').verbose_name
        self.assertEqual(date_name, 'date')

    def test_event_start_time_name(self):
        start_time_name = Event._meta.get_field('start_time').verbose_name
        self.assertEqual(start_time_name, 'start time')

    def test_event_end_time_name(self):
        end_time_name = Event._meta.get_field('end_time').verbose_name
        self.assertEqual(end_time_name, 'end time')

    def test_event_day_of_week_name(self):
        day_of_week_name = Event._meta.get_field('day_of_week').verbose_name
        self.assertEqual(day_of_week_name, 'day of week')

    def test_event_created_at_name(self):
        created_at_name = Event._meta.get_field('created_at').verbose_name
        self.assertEqual(created_at_name, 'created at')

    def test_event_updated_at_name(self):
        updated_at_name = Event._meta.get_field('updated_at').verbose_name
        self.assertEqual(updated_at_name, 'updated at')

    def test_event_category_max_length(self):
        max_length = Event._meta.get_field('category').max_length
        self.assertEqual(max_length, 100)

    def test_event_name_max_length(self):
        max_length = Event._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_event_location_max_length(self):
        max_length = Event._meta.get_field('location').max_length
        self.assertEqual(max_length, 100)

    def test_event_day_of_week_max_length(self):
        max_length = Event._meta.get_field('day_of_week').max_length
        self.assertEqual(max_length, 100)


    # I need to put some tests in here so that I can test the time created_at and updated_at
    # are recorded to confirm the parameters; I may put in freezegun, but the architecture
    # changes are beyond what I can do before a commit. Similarly, I need to test the ordering,
    # but it is multiple levels of organization, which is going to take a significant amount
    # of manual labor. I'm going to put an Issue in the GitHub repo.

    def test_event_string_method(self):
        expected_object_string = f'{self.event.category} -> {self.event.name}, {self.event.date}'
        self.assertEqual(self.event.__str__(), expected_object_string)
