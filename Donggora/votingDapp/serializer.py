from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Poll, Vote, Comment
User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, vallidated_data):
        return User.objects.create(**vallidated_data)

    def update(self, instance, vallidated_data):
        instance.name = vallidated_data.get('name', instance.name)
        instance.email = vallidated_data.get('email', instance.name)
        instance.save()
        return instance


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']


class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = ['author', 'title', 'content', 'valid_until', 'category']


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ['email', 'password']