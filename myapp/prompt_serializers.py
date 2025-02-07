from rest_framework import serializers

class PromptSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=100)
    prompt = serializers.CharField()