from django.contrib import admin
from .models import Asset, AssetType, Transaction, AccountPln


admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(Transaction)
admin.site.register(AccountPln)