from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'transactions', views.TransactionViewSet,basename='trasactions')
# router.register(r'companies', views.CompanyViewSet,basename="Company")
# router.register(r'price_histories', views.PriceHistoryViewSet,basename="price_histories")
# router.register(r'announcements', views.AnnouncementViewSet,basename="annoucements")
# router.register(r'news', views.NewsViewSet,basename="")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('companies/', views.CompanyList.as_view(),name="companies"),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(),name="company"),
    path('price_histories/', views.PriceHistoryList.as_view(),name="price_histories"),
    path('price_histories/<int:pk>/', views.PriceHistoryDetail.as_view(),name="price_history"),
    path('announcements/', views.AnnouncementList.as_view(),name="annoucements"),
    path('announcements/<int:pk>/', views.AnnouncementDetail.as_view(),name="annoucement"),
    path('news/', views.NewsList.as_view(),name="news"),
    path('news/<int:pk>/', views.NewsDetail.as_view(),name="new"),
    path('orders/', views.OrderCreateView.as_view(),name='orders'),
    path('portfolio/', views.PortfolioView.as_view(),name='portfolio'),
    

]