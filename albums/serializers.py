from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from .models import Album


class AlbumSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
