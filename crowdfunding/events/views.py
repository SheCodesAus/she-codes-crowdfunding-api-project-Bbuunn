from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Event
from .serializers import EventSerializer, EventDetailSerializer
from .permissions import IsOwnerOrReadOnly
class EventList(APIView):
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    def get(self, request):
        events = Event.objects.all()
        #python into json
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request): #create into model instance
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        # 'incorrect' responses
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EventDetail(APIView):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]
    
    def get_object(self, pk): #pk = event id
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event) #turning into json
        return Response(serializer.data)
    
    def put(self, request, pk):
        event = self.get_object(pk)
        data = request.data
        serializer = EventDetailSerializer(
            instance=event,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttendanceList(APIView): #can use event id as pk as argument for
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_object(self, pk): #pk = event id
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

   
    def post(self, request, pk):
        event = self.get_object(pk)
        if request.user in event.attendees.all():
            event.attendees.remove(request.user)
            return Response("You are now attending the event.")
        else:
            event.attendees.add(request.user)
        return Response("You are no longer attending the event.",status=status.HTTP_200_OK)
       