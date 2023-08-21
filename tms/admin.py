from django.contrib import admin
from .models import Company, PriceHistory, Announcement, News, Fund, Payment, Purchase, Sold

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'ltp')

@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('company', 'open_price', 'close_price', 'low_price', 'high_price', 'qty', 'change')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('amount', 'user')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'user')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('company', 'qty', 'buy_price', 'user')

@admin.register(Sold)
class SoldAdmin(admin.ModelAdmin):
    list_display = ('company', 'qty', 'sold_price', 'user')
