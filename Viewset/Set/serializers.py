from rest_framework.serializers import ModelSerializer
from.models import Srirama
class SriramaSerializers(ModelSerializer):
    class Meta:
        model=Srirama
        fields="__all__"