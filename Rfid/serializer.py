from rest_framework import routers, serializers, viewsets

from Rfid.models import Rfid

class RfidSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rfid
        fields = ('__all__')