from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Poll, Vote, Comment
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'poll']

    def create(self, vallidated_data):
        return Comment.objects.create(**vallidated_data)


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['author', 'title', 'content', 'valid_until', 'category', 'pros', 'cons']

    def create(self, vallidated_data):
        return Poll.objects.create(**vallidated_data)

    def update(self, vallidated_data):
        instance.pros = vallidated_data.get('pros', instance.pros)
        instance.cons = vallidated_data.get('cons', instance.cons)
        instance.save()
        return instance


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['email', 'password']