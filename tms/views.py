from django.shortcuts import render
from rest_framework import generics,status
from .models import *
from .serializers import *
from django_filters  import rest_framework as d_filters
from rest_framework import filters,viewsets
from .services import OrderService  # Import the OrderService class you created
from  rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CompanyList(generics.ListAPIView):
    serializer_class=CompanySerializer
    queryset=Company.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields=['name','symbol']


class CompanyDetail(generics.RetrieveAPIView):
    serializer_class=CompanySerializer
    queryset=Company.objects.prefetch_related('price_histories').all()




class PriceHistoryList(generics.ListAPIView):
    serializer_class=PriceHistorySerializer
    queryset=PriceHistory.objects.all()
    filter_backends = (d_filters.DjangoFilterBackend,)
    filterset_fields=[
        'company',
        'open_price',
        'close_price',
        'low_price',
        'high_price',
        'qty',
        'change',
                      
    ]

class PriceHistoryDetail(generics.RetrieveAPIView):
    serializer_class=PriceHistorySerializer
    queryset=PriceHistory.objects.select_related('company').all()


class AnnouncementList(generics.ListAPIView):
    serializer_class=AnnouncementSerializer
    queryset=Announcement.objects.all()


class AnnouncementDetail(generics.RetrieveAPIView):
    serializer_class=AnnouncementSerializer
    queryset=Announcement.objects.select_related('company').all()
    filter_backends = (d_filters.DjangoFilterBackend,)
    filterset_fields=[
        'company',
        'date',
        'title',
        'description',
                      
    ]


class NewsList(generics.ListAPIView):
    serializer_class=NewsSerializer
    queryset=News.objects.all()


class NewsDetail(generics.RetrieveAPIView):
    serializer_class=NewsSerializer
    queryset=News.objects.select_related('company').all()
    filter_backends = (d_filters.DjangoFilterBackend,)
    filterset_fields=[
        "date",
        "title",
        "description",                 
    ]



class OrderCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order=serializer.validated_data
            # order=request.data.get('order_type')
            # order = serializer.save()

            try:
                if order['order_type'] == 'buy':
                    pass
                    OrderService.execute_buy_order(order,request.user,serializer)
                elif order['order_type'] == 'sell':
                    # Call the corresponding sell execution logic
                    
                    OrderService.execute_sell_order(order,request.user,serializer)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class PortfolioView(generics.ListAPIView):
    serializer_class=PortfolioSerializer
    
    def get_queryset(self):
        return Portfolio.objects \
            .select_related('company') \
            .filter(user=self.request.user)
    
    