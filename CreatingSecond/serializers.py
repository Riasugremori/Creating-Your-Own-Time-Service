from rest_framework import serializers
from .models import CurrentTime

class TimeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentTime
        fields = '__all__'
