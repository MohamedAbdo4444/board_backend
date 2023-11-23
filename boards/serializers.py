from rest_framework import serializers
from .models import *


class BoardSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TopicSerlializer(serializers.ModelSerializer):
    boards = BoardSerlializer(many=True, read_only = True)
    board_name = serializers.CharField(source="board.name", required = False)
    creater_name = serializers.CharField(source="created_by.username", required = False)
    class Meta:
        model = Topic
        fields = '__all__'


class PostSerlializer(serializers.ModelSerializer):
    topics = TopicSerlializer(many= True, read_only=True, required = False)
    class Meta:
        model = Post
        fields = '__all__'