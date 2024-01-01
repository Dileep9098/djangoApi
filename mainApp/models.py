from django.db import models

class Invoice(models.Model):
    invoiceF=models.CharField(max_length=10,default="", null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    customerName=models.CharField(max_length=20)
    

    def __str__(self):
        return self.customerName

class InvoiceDetail(models.Model):
    description=models.CharField(max_length=200,default="", null=True, blank=True)
    quantity=models.IntegerField(default="", null=True, blank=True)
    unit_price=models.IntegerField(default="", null=True, blank=True)
    price=models.IntegerField(default="", null=True, blank=True)
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description




    





