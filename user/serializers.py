from user.models import UserInfo, UserGroup
from rest_framework import serializers


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username', 'password', 'email', 'mobile')


class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('__all__')
