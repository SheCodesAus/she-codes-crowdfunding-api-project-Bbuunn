from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('attendances/', views.AttendanceList.as_view()),
    path('attendances/', views.AttendanceCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)