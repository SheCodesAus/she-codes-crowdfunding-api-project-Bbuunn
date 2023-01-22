from rest_framework import serializers
from .models import Event, Attendance

class AttendanceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user = serializers.CharField(max_length=200) #q: will this need updating?
    event_id = serializers.IntegerField()

    def create(self, validated_data): #Do you "create" attendance?
        return Attendance.objects.create(**validated_data)


class EventSerializer(serializers.Serializer): #we need to give it fields in models
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    location = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField(read_only=True)
    online = serializers.BooleanField()
    is_open = serializers.BooleanField(required=False) #do I add (default=True)
    image = serializers.URLField()
    min_attendees=serializers.IntegerField()
    max_attendees=serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class EventDetailSerializer(EventSerializer):
    #another type of project serializer
    attendances = AttendanceSerializer(many=True, read_only=True)