from django.db import models


class Wallet(models.Model):
    asset = models.CharField("Asset", max_length=256)
    quantity = models.FloatField()


class History(models.Model):
    transaction_type = models.CharField("Transaction type", max_length=64)
    transaction_datetime = models.DateTimeField(auto_now_add=True)


class Balance(models.Model):
    pass


class Transactions(models.Model):
    pass


class Types(models.Model):
    pass


class AssetTypes(models.Model):
    pass
