from rest_framework import serializers
from parse_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # Make fields from the Post model (parse_app application) to serializer output
        fields = ['title', 'url', 'created']
