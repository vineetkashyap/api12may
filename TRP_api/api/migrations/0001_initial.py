# Generated by Django 3.0.5 on 2021-05-12 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tranage_Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=50)),
                ('alternate_mobile_number', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('aadhar_number', models.CharField(max_length=50, unique=True)),
                ('pan_number', models.CharField(max_length=50, unique=True)),
                ('bank_account_name', models.CharField(max_length=50)),
                ('bank_account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('aadhar_front', models.FileField(upload_to='media')),
                ('aadhar_back', models.FileField(upload_to='media')),
                ('pan_card_front', models.FileField(upload_to='media')),
                ('cancelled_cheque', models.FileField(upload_to='media')),
                ('photo', models.FileField(upload_to='media')),
                ('sign', models.FileField(upload_to='media')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('registered_by', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransporterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=500)),
                ('contact_person', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=500)),
                ('alternarte_number', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=500)),
                ('gstin', models.CharField(max_length=50, unique=True)),
                ('pan_number', models.CharField(max_length=50, unique=True)),
                ('bank_account_name', models.CharField(max_length=100)),
                ('bank_account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('gstin_certificate', models.FileField(upload_to='media')),
                ('pan_card_front', models.FileField(upload_to='media')),
                ('cancelled_cheque', models.FileField(upload_to='media')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('registered_by', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TruckOwnerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=50)),
                ('alternate_mobile_number', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('aadhar_number', models.CharField(max_length=50, unique=True)),
                ('pan_number', models.CharField(max_length=50, unique=True)),
                ('bank_account_name', models.CharField(max_length=50)),
                ('bank_account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('aadhar_front', models.FileField(upload_to='media')),
                ('aadhar_back', models.FileField(upload_to='media')),
                ('pan_card_front', models.FileField(upload_to='media')),
                ('cancelled_cheque', models.FileField(upload_to='media')),
                ('photo', models.FileField(upload_to='media')),
                ('sign', models.FileField(upload_to='media')),
                ('register_on', models.DateField(auto_now_add=True)),
                ('register_by', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleRegistraionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_registration_number', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_contact_number', models.CharField(max_length=500)),
                ('vehicle_model_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('wheel_type', models.CharField(max_length=50)),
                ('maximum_load_capacity', models.CharField(max_length=50)),
                ('insurance_expiry_date', models.CharField(max_length=100)),
                ('preference_product', models.CharField(max_length=50)),
                ('preferred_location', models.CharField(max_length=50)),
                ('vehicle_front_photo', models.FileField(upload_to='media')),
                ('vehicle_back_photo', models.FileField(upload_to='media')),
                ('vehicle_left_photo', models.FileField(upload_to='media')),
                ('vehicle_right_photo', models.FileField(upload_to='media')),
                ('registration_certificate', models.FileField(upload_to='media')),
                ('fitness_certificate', models.FileField(upload_to='media')),
                ('pollution_certificate', models.FileField(upload_to='media')),
                ('permit_certificate', models.FileField(upload_to='media')),
                ('insurance_certificate', models.FileField(upload_to='media')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('registered_by', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
                ('truck_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TruckOwnerModel')),
            ],
        ),
        migrations.CreateModel(
            name='DriverRegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=50)),
                ('alternate_number', models.CharField(max_length=50)),
                ('home_mobile_number', models.CharField(max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('aadhar_number', models.CharField(max_length=50, unique=True)),
                ('pan_number', models.CharField(max_length=50, unique=True)),
                ('dl_number', models.CharField(max_length=50, unique=True)),
                ('dl_type', models.CharField(max_length=50)),
                ('dl_expiry_date', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('bank_account_name', models.CharField(max_length=50)),
                ('bank_account_number', models.CharField(max_length=200)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='media')),
                ('aadhar_front', models.FileField(upload_to='media')),
                ('aadhar_back', models.FileField(upload_to='media')),
                ('pan_front', models.FileField(upload_to='media')),
                ('dl_front', models.FileField(upload_to='media')),
                ('dl_back', models.FileField(upload_to='media')),
                ('passbook_or_cheque', models.FileField(upload_to='media')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('registered_by', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
                ('truck_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TruckOwnerModel')),
            ],
        ),
    ]
