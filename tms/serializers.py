from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=PriceHistory
        fields='__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Announcement
        fields='__all__'
        


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'



class CompanySerializer(serializers.ModelSerializer):
    price_histories=PriceHistorySerializer(many=True)
    announcements=AnnouncementSerializer(many=True)
    news=NewsSerializer(many=True)
    
    class Meta:
        model=Company
        fields='__all__'
        
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'



User = get_user_model()

class UserCreateSerializer(DjoserUserCreateSerializer):
    username = serializers.CharField(required=True)

    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        fields = ('email', 'username', 'password', 'password2')
        
        
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'