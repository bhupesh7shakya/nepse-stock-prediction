from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'companies', views.CompanyViewSet,basename="Company")
# router.register(r'price_histories', views.PriceHistoryViewSet,basename="price_histories")
# router.register(r'announcements', views.AnnouncementViewSet,basename="annoucements")
# router.register(r'news', views.NewsViewSet,basename="")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('companies/', views.CompanyList.as_view(),name="Company"),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(),name="Company"),
    # path('price_histories/', views.PriceHistoryViewSet.as_view(),name="price_histories"),
    # path('price_histories/<int:pk>/', views.PriceHistoryViewSet.as_view(),name="price_histories"),
    # path('announcements/', views.AnnouncementViewSet.as_view(),name="annoucements"),
    # path('announcements/<int:pk>/', views.AnnouncementViewSet.as_view(),name="annoucements"),
    # path('news/', views.NewsViewSet.as_view(),name=""),
    # path('news/<int:pk>/', views.NewsViewSet.as_view(),name=""),

]