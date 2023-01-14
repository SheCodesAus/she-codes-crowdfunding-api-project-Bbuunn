from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer
from django.http import Http404
from rest_framework import status

class ProjectList(APIView): #handling get requests
    def get(self, request):
        projects = Project.objects.all()
        #python into json
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request): #create into model instance
        serializer = ProjectSerializer(data=request.data)
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


class ProjectDetail(APIView):
    def get_object(self, pk): #pk = project id
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project) #turning into json
        return Response(serializer.data)

class PledgeList(APIView): #can use project id as pk as argument for
    def get(self, request):
        pledges = Pledge.objects.all() #list of pledges
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
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