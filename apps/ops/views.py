from django.shortcuts import render
from .models import JobsList
from .serializers import JobsListSerializer
from rest_framework import viewsets


class JobsListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = JobsList.objects.all()
    serializer_class = JobsListSerializer
