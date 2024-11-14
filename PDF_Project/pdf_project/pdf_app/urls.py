from django.contrib import admin
from django.urls import path
from .views import handle_weasy_form

urlpatterns = [
    path('generate-pdf/', handle_weasy_form, name='handle_txn_true'),
    path('', handle_weasy_form, name='handle_weasy_form'),
    path('admin/', admin.site.urls),

]
