from django.db import models

# Create your models here.
class TruckOwnerModel(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    alternate_mobile_number = models.CharField(max_length=50)
    email_id  = models.EmailField(max_length=254,unique=True)
    address  = models.CharField(max_length=50)
    aadhar_number =models.CharField( max_length=50)
    pan_number = models.CharField(max_length=50)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    aadhar_xerox = models.FileField(upload_to='media', max_length=100)
    pan_card_xerox = models.FileField(upload_to='media', max_length=100)
    cancelled_cheque_xerox = models.FileField(upload_to='media', max_length=100)
    photo = models.FileField(upload_to='media', max_length=100)
    sign = models.FileField(upload_to='media', max_length=100)
    register_on = models.DateField(auto_now_add=True)
    register_by = models.CharField(max_length=50)