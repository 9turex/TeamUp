from rest_framework import serializers
from .models import *


class CreateTestSerializer(serializers.Serializer):
    login = serializers.CharField(min_length=10, max_length=10)


class IqTestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    login = serializers.CharField(min_length=10, max_length=10)
    score = serializers.IntegerField(min_value=1, max_value=50)
    finish_time = serializers.DateTimeField(read_only=True)


class EqTestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    login = serializers.CharField(min_length=10, max_length=10)
    score = serializers.IntegerField(min_value=1, max_value=50)
    answer = serializers.CharField(max_length=5, min_length=5)
    finish_time = serializers.DateTimeField(read_only=True)


class AllAnswerSerializer(serializers.ModelSerializer):
    iq_result = IqTestSerializer()
    eq_result = EqTestSerializer()

    class Meta:
        model = CreateTestSerializer()
        fields = ('all', 'iq_result', 'eq_result')
