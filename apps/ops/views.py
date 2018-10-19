from django.shortcuts import render
from ops.models import JobsList
from rest_framework import viewsets
from ops.serializers import JobsListSerializer


class JobsListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = JobsList.objects.all()
    serializer_class = JobsListSerializer
