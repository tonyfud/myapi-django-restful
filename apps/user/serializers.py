from .models import UserInfo, UserGroup
from rest_framework import serializers


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id','username', 'mobile', 'realname', 'email', 'status', 'last_login_time')
        depth = 1
        #exclude = ('password',)
        # fields = ('id','username')


class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'
