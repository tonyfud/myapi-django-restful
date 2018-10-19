from cmdb.models import Server, Host
from rest_framework import serializers


class ServerSerializer(serializers.ModelSerializer):
    """
    服务器序列化
    """

    class Meta:
        model = Server
        fields = ('id', 'server_name', 'server_num', 'brand', 'model', 'cpus',
                  'ram', 'disk', 'product_date', 'status', 'create_date',
                  'update_time')
