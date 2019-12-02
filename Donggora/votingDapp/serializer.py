from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Poll, Vote, Comment
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'gender', 'phone', 'department']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.name)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'poll']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['author', 'title', 'content', 'valid_until', 'category', 'pros', 'cons', 'contract']

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, validated_data):
        instance.pros = validated_data.get('pros', instance.pros)
        instance.cons = validated_data.get('cons', instance.cons)
        instance.save()
        return instance


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['email', 'password']