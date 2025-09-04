import factory

from events import models


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event

    category = factory.Faker('word')
    name = factory.Faker('word')
    description = factory.Faker('sentence')
    location = factory.Faker('word')
    date = factory.Faker('date')
    start_time = factory.Faker('time')
    end_time = factory.Faker('time')
