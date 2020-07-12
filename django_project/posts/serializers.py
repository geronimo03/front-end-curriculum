from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')

    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'content', 'view_count', '_type', 'image', 'created_at', 'updated_at', 'highlight')
        user = serializers.ReadOnlyField(source='user.username')

        def create(self, validated_data):
            return Post.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.view_count = validated_data.get('view_count', instance.view_count)
            instance.image = validated_data.get('image', instance.image)
            instance.created_at = validated_data.get('created_at', instance.created_at)
            instance.updated_at = validated_data.get('updated_at', instance.updated_at)

            instance.save()
            return instance
