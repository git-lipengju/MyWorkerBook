from django.contrib import admin
from control_hedge import models
class symbol_config_admin(admin.ModelAdmin):
    list_display = ('symbol', 'amount', 'price', 'askPrice', 'bidPrice', 'bidAmount', 'askAmount', 'minAmount', 'maxAmount', 'dealMaxAmount', 'dealProportion', 'dealWarningAmount', 'status', 'depthStep')
# Register your models here.
class order_info_admin(admin.ModelAdmin):
    list_display = ('jc_order_id', 'symbol', 'base_symbol', 'quote_symbol', 'price', 'volume', 'side', 'jc_ctime', 'jc_cdate', 'ome_name', 'ome_order_id', 'ome_price', 'ome_deal_price', 'ome_deal_volume', 'ome_volume', 'fee', 'ome_ctime', 'ome_mtime', 'status', 'ctime', 'mtime',)
admin.site.register(models.Person)
admin.site.register(models.ApiInfo)
admin.site.register(models.SymbolConfig, symbol_config_admin)
admin.site.register(models.OrderInfo, order_info_admin)
