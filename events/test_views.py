from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase

from events.factories import EventFactory
from events.models import Event

factory = APIRequestFactory()
client = APIClient()
request = factory.get("/events/")


class TestEventBulkGet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.event1 = EventFactory.create()
        cls.event2 = EventFactory.create()
        cls.event3 = EventFactory.create()
        cls.event1.date = "1981-02-16"
        cls.event2.date = "1982-02-16"
        cls.event3.date = "1983-02-16"
        cls.event1.save()
        cls.event2.save()
        cls.event3.save()

    @classmethod
    def tearDownTestData(cls):
        Event.objects.all().delete()

    def test_event_bulk_get_returns_correct_number(self):
        response = client.get("/events/")
        self.assertEqual(len(response.data[ "events" ]), 3)

    def test_event_bulk_get_returns_correct_data(self):
        response = client.get("/events/")
        self.assertEqual(response.data[ "events" ][ 0 ][ "category" ], self.event1.category)
        self.assertEqual(response.data[ "events" ][ 1 ][ "category" ], self.event2.category)
        self.assertEqual(response.data[ "events" ][ 2 ][ "category" ], self.event3.category)
