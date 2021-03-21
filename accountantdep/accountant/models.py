from django.db import models


ASSET_TYPES = (
    ('cash', 'gotówka'),
    ('stock', 'akcje'),
    ('bond', 'obligacje'),
    ('crypto', 'krypto'),
    ('commodity', 'surowce')
)


TRANSACTION_TYPES = (
    ('buy', 'kup'),
    ('sell', 'sprzedaj'),
)

ACCOUNT_TRANSACTION_TYPE = (
    ('deposit', 'wpłata'),
    ('withdraw', 'wypłata'),
    ('buy', 'kup'),
    ('sell', 'sprzedaj'),
)


class AccountPln(models.Model):
    balance = models.FloatField()
    transaction_type = models.CharField(
        max_length=8, 
        choices=ACCOUNT_TRANSACTION_TYPE
        )
    total_balance = models.FloatField()

    def __str__(self):
        return '{} $'.format(self.total_balance)


class Transaction(models.Model):
    asset = models.CharField(max_length=64)
    quantity = models.FloatField()
    price = models.FloatField()
    transaction_type = models.CharField(max_length=16, choices=TRANSACTION_TYPES)
    transaction_date = models.DateTimeField(auto_now_add=True)


class Asset(models.Model):
    asset = models.CharField("Asset", max_length=256)
    quantity = models.FloatField()

    def __str__(self):
        return self.asset


class AssetType(models.Model):
    asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE)
    asset_type = models.CharField(max_length=16, choices=ASSET_TYPES)
