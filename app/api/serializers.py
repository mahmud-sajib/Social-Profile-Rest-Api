from rest_framework import serializers
from app.models import Status
from authentication.api.serializers import UserInfoDisplaySerializer

# Status Model Serializer
class StatusModelSerializer(serializers.ModelSerializer):
    # importing nested User Serializer
    author = UserInfoDisplaySerializer(read_only=True)
    
    class Meta:
        model = Status
        fields = ['id', 'author', 'content', 'image']
        read_only_fields = ['author']

    # validate serializer content length
    def validate_content(self, value):
        if len(value) > 240:
            raise serializers.ValidationError("Content is too long.")
        
        return value

    # validate serializer content or image upload
    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None

        image = data.get('image', None)

        if content is None and image is None:
            raise serializers.ValidationError("Content or Image is required")
        
        return data
