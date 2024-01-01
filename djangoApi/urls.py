
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('getEmployeeRecord/',views.getEmpolyeeRecord)
    path('invoice/',include('mainApp.urls'))
]
