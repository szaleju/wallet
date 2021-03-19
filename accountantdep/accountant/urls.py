from django.urls import path
from .views import accountant_view


app_name='accountant'
urlpatterns=[
    path('', accountant_view, name='accountant')
]