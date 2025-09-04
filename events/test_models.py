from django.test import TestCase

from events.models import Event
from events.factories import EventFactory

class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        EventFactory.create()

    def test_event_category_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('category').max_length
        self.assertIs(max_length, 100)

    def test_event_name_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('name').max_length
        self.assertIs(max_length, 100)

    def test_event_location_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('location').max_length
        self.assertIs(max_length, 100)

    def test_event_string_method(self):
        event = Event.objects.get(id=1)
        expected_object_string = f'{event.category} -> {event.name}, {event.date}'
        self.assertIs(event.__str__(), expected_object_string)
