from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/create/', views.EventCreate.as_view()),
    # path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    # path('pledges/', views.PledgeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
