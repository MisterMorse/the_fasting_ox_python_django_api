from django.test import TestCase

from events.models import Event
from events.factories import EventFactory

class EventFactoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.event1 = EventFactory.create()
        cls.event2 = EventFactory.create()

    @classmethod
    def tearDownTestData(cls):
        Event.objects.all().delete()

    def test_event_factory_uses_correct_model(self):
        self.assertIsInstance(self.event1, Event)

    def test_event_factory_creates_event_with_category(self):
        self.assertNotEqual(self.event1.category, '')

    def test_event_factory_creates_event_with_unique_category(self):
        self.assertNotEqual(self.event1.category, self.event2.category)
        
    def test_event_factory_creates_event_with_name(self):
        self.assertNotEqual(self.event1.name, '')

    def test_event_factory_creates_event_with_unique_name(self):
        self.assertNotEqual(self.event1.name, self.event2.name)

    def test_event_factory_creates_event_with_description(self):
        self.assertNotEqual(self.event1.description, '')

    def test_event_factory_creates_event_with_unique_description(self):
        self.assertNotEqual(self.event1.description, self.event2.description)

    def test_event_factory_creates_event_with_location(self):
        self.assertNotEqual(self.event1.location, '')

    def test_event_factory_creates_event_with_unique_location(self):
        self.assertNotEqual(self.event1.location, self.event2.location)

    def test_event_factory_creates_event_with_date(self):
        self.assertNotEqual(self.event1.date, '')

    def test_event_factory_creates_event_with_unique_date(self):
        self.assertNotEqual(self.event1.date, self.event2.date)

    def test_event_factory_creates_event_with_start_time(self):
        self.assertNotEqual(self.event1.start_time, '')

    def test_event_factory_creates_event_with_unique_start_time(self):
        self.assertNotEqual(self.event1.start_time, self.event2.start_time)

    def test_event_factory_creates_event_with_end_time(self):
        self.assertNotEqual(self.event1.end_time, '')

    def test_event_factory_creates_event_with_unique_end_time(self):
        self.assertNotEqual(self.event1.end_time, self.event2.end_time)

    def test_event_factory_creates_event_with_day_of_week(self):
        self.assertNotEqual(self.event1.day_of_week, '')

    def test_event_factory_creates_event_with_unique_day_of_week(self):
        self.assertNotEqual(self.event1.day_of_week, self.event2.day_of_week)

    def test_event_factory_creates_event_with_created_at(self):
        self.assertNotEqual(self.event1.created_at, '')

    def test_event_factory_creates_event_with_unique_created_at(self):
        self.assertNotEqual(self.event1.created_at, self.event2.created_at)

    def test_event_factory_creates_event_with_updated_at(self):
        self.assertNotEqual(self.event1.updated_at, '')

    def test_event_factory_creates_event_with_unique_updated_at(self):
        self.assertNotEqual(self.event1.updated_at, self.event2.updated_at)
