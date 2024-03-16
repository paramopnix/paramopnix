from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewset, status
from rest_framework.response import Response
from .models import Deposit, Payment
from .serializers import DepositSerializer, PaymentSerializer
import requests
from django.conf import settings


class DepositViewSet(Viewsets.ModelViewset):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        amount = serializer.validated_data['amount']
