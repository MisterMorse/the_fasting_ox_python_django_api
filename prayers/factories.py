import factory

from prayers import models


class PrayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Prayer

    category = factory.Faker("word")
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    created_at = factory.Faker("date_time")
    updated_at = factory.Faker("date_time")
