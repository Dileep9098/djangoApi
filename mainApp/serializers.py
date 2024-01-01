from .models import Invoice,InvoiceDetail
from rest_framework import serializers

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Invoice
        fields='__all__'
        # fields=['date','invoiceF','customerName']

class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice=InvoiceSerializer(many=True,read_only=True)
    class Meta:
        model= InvoiceDetail
        fields='__all__'

    def update(self,instance,validateData):
        if("invoiceF" in validateData and validateData['invoiceF']!=''):
            instance.invoiceF=validateData['invoiceF']
        if("customerName" in validateData and validateData['invoiceF']!=''):
            instance.customerName=validateData['customerName']
        if("description" in validateData and validateData['invoiceF']!=''):
            instance.description=validateData['description']
        if("quantity" in validateData and validateData['quantity']!=''):
            instance.quantity=validateData['quantity'] 
        if("unit_price" in validateData and validateData['unit_price']!=''):
            instance.unit_price=validateData['unit_price']         
        if("price" in validateData and validateData['price']!=''):
            instance.price=validateData['price']         
              

        # fields=['description','quantity','unit_price','price','invoice']