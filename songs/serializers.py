from rest_framework.serializers import ModelSerializer
from .models import Song


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
        read_only_fields = ["album_id"]

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
