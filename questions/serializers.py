from rest_framework import serializers, status

class CreateQuestion(serializers.ModelSerializer):
    question = serializers.CharField(max_length=128, min_length=6)

class VoteForAnswer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=128, min_length=6)
