
from django.contrib import admin
from django.urls import path
from .views import InvoiceView,InvoiceDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('getEmployeeRecord/',views.getEmpolyeeRecord)
    path('invoice/',InvoiceView.as_view()),
    path('invoiceDetail/',InvoiceDetailView.as_view())
]
