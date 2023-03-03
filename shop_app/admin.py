from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from .models import *


class TgUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_firstname', 'user_id', 'user_username', 'user_is_referral', 'user_referrals_count',
                    'user_referrals_balance', 'is_banned', 'reg_date']
    list_filter = ['id', 'user_firstname', 'user_id', 'user_username', 'is_banned', 'reg_date', 'user_referrals_count']
    list_editable = ['is_banned']
    search_fields = ['id', 'user_firstname', 'user_id', 'user_username', 'is_banned', 'reg_date',
                     'user_referrals_balance']
    fields = ['user_firstname', 'user_id', 'user_username', 'user_is_referral', 'user_referrals_count',
              'user_referrals_balance', 'is_banned', 'reg_date']
    readonly_fields = ['reg_date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_name', 'cat_create_date']
    list_filter = ['id', 'cat_name', 'cat_create_date']
    list_editable = ['cat_name']
    search_fields = ['id', 'cat_name', 'cat_create_date']
    fields = ['cat_name', 'cat_create_date']
    readonly_fields = ['cat_create_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'prod_name', 'prod_cat', 'get_html_photo', 'prod_price', 'prod_create_date']
    list_filter = ['id', 'prod_name', 'prod_cat', 'prod_price', 'prod_create_date']
    list_editable = ['prod_name', 'prod_cat', 'prod_price']
    search_fields = ['id', 'prod_name', 'prod_cat', 'prod_price', 'prod_create_date']
    fields = ['prod_name', 'prod_cat', 'prod_descr', 'get_html_photo', 'prod_photo', 'prod_price',
              'prod_create_date']
    readonly_fields = ['prod_create_date', 'get_html_photo']

    def get_html_photo(self, object):
        if object.prod_photo:
            return mark_safe(f"<img src='{object.prod_photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_user', 'order_prod', 'order_prod_quan', 'order_user_phone', 'order_delivery_type',
                    'order_pay_type', 'order_address', 'order_price', 'order_create_date']
    list_filter = ['id', 'order_user', 'order_delivery_type', 'order_pay_type', 'order_prod_quan', 'order_prod',
                   'order_price', 'order_create_date']
    search_fields = ['id', 'order_user', 'order_prod', 'order_user_phone', 'order_create_date', 'order_price',
                     'order_prod_quan']


class TgAdminAdmin(admin.ModelAdmin):
    list_display = ['id', 'admin_name', 'admin_id', 'admin_created_date']
    list_filter = ['id', 'admin_name', 'admin_id', 'admin_created_date']
    search_fields = ['id', 'admin_name', 'admin_id', 'admin_created_date']


class TgBotAdmin(admin.ModelAdmin):
    list_display = ['id', 'bot_token', 'bot_name', 'bot_created_date']
    list_filter = ['id', 'bot_created_date']
    readonly_fields = ['bot_code']
    search_fields = ['id', 'bot_token', 'bot_name', 'bot_created_date']


class PercentAdmin(admin.ModelAdmin):
    list_display = ['id', 'percent', 'min_sum']
    list_editable = ['percent', 'min_sum']

    def has_add_permission(self, request):
        return False

        # This will help you to disable delete functionaliyt

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Percent, PercentAdmin)
admin.site.register(TgBot, TgBotAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TgUser, TgUserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(TgAdmin, TgAdminAdmin)
admin.site.unregister(Group)

admin.site.site_title = 'Админ панель'
admin.site.site_header = 'Админ панель'
