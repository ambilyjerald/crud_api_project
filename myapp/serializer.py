from rest_framework import serializers

from myapp.models import staff


class staff_serializer(serializers.ModelSerializer):
    class Meta:
        model=staff
        fields=('__all__')
