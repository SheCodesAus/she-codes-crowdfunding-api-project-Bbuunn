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
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
