from rest_framework import serializers

from prayers.models import Prayer


class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayer
        fields = "__all__"
