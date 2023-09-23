from django.contrib import admin
from .models import Company, PriceHistory, Announcement, News, Fund, Payment,Portfolio,Order,Transaction

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



# @admin.register(Sold)
# class SoldAdmin(admin.ModelAdmin):
#     list_display = ('company', 'qty', 'price', 'user')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('company', 'qty', 'price', 'user', 'order_type')
    list_filter = ('order_type',)
    search_fields = ('company__name', 'user__username')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'quantity', 'price', 'timestamp', 'transaction_type')
    list_filter = ('transaction_type',)
    search_fields = ('company__name', 'user__username')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'quantity')
    search_fields = ('user__username', 'company__name')
