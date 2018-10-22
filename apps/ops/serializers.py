from .models import JobsList
from rest_framework import serializers


class JobsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobsList
        fields = '__all__'


