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
