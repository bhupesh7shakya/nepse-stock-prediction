from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.


class CompanyList(generics.ListAPIView):
    serializer_class=CompanySerializer
    queryset=Company.objects.all()


class CompanyDetail(generics.RetrieveAPIView):
    serializer_class=CompanySerializer
    queryset=Company.objects.prefetch_related('price_histories').all()



class PriceHistoryList(generics.ListAPIView):
    serializer_class=PriceHistorySerializer
    queryset=PriceHistory.objects.all()

class PriceHistoryDetail(generics.RetrieveAPIView):
    serializer_class=PriceHistorySerializer
    queryset=PriceHistory.objects.select_related('company').all()


class AnnouncementList(generics.ListAPIView):
    serializer_class=AnnouncementSerializer
    queryset=Announcement.objects.all()


class AnnouncementDetail(generics.RetrieveAPIView):
    serializer_class=AnnouncementSerializer
    queryset=Announcement.objects.select_related('company').all()



class NewsList(generics.ListAPIView):
    serializer_class=NewsSerializer
    queryset=News.objects.all()


class NewsDetail(generics.RetrieveAPIView):
    serializer_class=NewsSerializer
    queryset=News.objects.select_related('company').all()
