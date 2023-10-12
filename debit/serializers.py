from rest_framework import serializers

from .models import credit, data


class CreditSerializer(serializers.ModelSerializer):
    id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = credit
        fields = "__all__"
        
        
class DebitSerializer(serializers.ModelSerializer):
    id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = data
        fields = "__all__"
        
    def create(self, validated_data):
        return data.objects.create(**validated_data)