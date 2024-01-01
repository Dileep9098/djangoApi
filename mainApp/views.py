from django.shortcuts import render
from .serializers import InvoiceSerializer,InvoiceDetailSerializer
from rest_framework import generics
from .models import Invoice,InvoiceDetail



class InvoiceView(generics.ListCreateAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer

class InvoiceDetailView(generics.ListCreateAPIView):
    queryset=InvoiceDetail.objects.all()
    serializer_class=InvoiceDetailSerializer


