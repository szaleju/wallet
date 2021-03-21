from django.contrib import admin
from .models import Asset, AssetType, Transaction, AccountPln


class AccountPlnAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_type', 'balance', 'total_balance')


admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(Transaction)
admin.site.register(AccountPln, AccountPlnAdmin)