from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.Serializer): #we need to give it fields in models
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    image = serializers.URLField()
    is_open = serializers.BooleanField(required=False) #do I add (default=True)
    created_at = serializers.DateTimeField(read_only=True)
    online = serializers.BooleanField()
    location = serializers.CharField(max_length=200)
    min_attendees=serializers.IntegerField()
    max_attendees=serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.id')
    attendees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class EventDetailSerializer(EventSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.created_at = validated_data.get('created_at',instance.created_at)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.online = validated_data.get('online', instance.online)
        instance.location = validated_data.get('location', instance.location)
        instance.min_attendees = validated_data.get('min_attendees', instance.min_attendees)
        instance.max_attendees = validated_data.get('max_attendees', instance.max_attendees)
        instance.save()
        return instance
