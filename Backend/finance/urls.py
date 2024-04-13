from django.urls import path
from .views import *

urlpatterns = [
    path('input_transaction/', input_transaction, name='input_transaction'),
    path('insights/', insights, name='insights'),
    path('api/insights/', insights_detail, name='insights_details'),
    path('api/transactions/', create_transaction, name='create_transaction'),
]