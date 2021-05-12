from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(TruckOwnerModel)
class TruckOwnerModelAdmin(admin.ModelAdmin):
    cancelled_cheque_xerox = models.FileField(upload_to='media', max_length=100)
    sign = models.FileField(upload_to='media', max_length=100)
    list_display = ['id','name','father_name','mobile_number','alternate_mobile_number','email_id','address','aadhar_number','pan_number','bank_account_name','bank_account_number','ifsc_code','bank_name','branch_name','aadhar_xerox','pan_card_xerox','cancelled_cheque_xerox','photo','photo','sign']