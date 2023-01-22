from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, Attendance
from .serializers import EventSerializer, AttendanceSerializer, EventDetailSerializer
from django.http import Http404
from rest_framework import status

class EventList(APIView): #handling get requests
    def get(self, request):
        events = Event.objects.all()
        #python into json
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventCreate(APIView):
    def post(self, request): #create into model instance
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        # 'incorrect' responses
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EventtDetail(APIView):
    def get_object(self, pk): #pk = project id
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event) #turning into json
        return Response(serializer.data)

class AttendanceList(APIView): #can use project id as pk as argument for
    def get(self, request):
        attendances = Attendance.objects.all() #list of attendances
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

class AttendanceCreate(APIView):
    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )