# Generated by Django 3.2.7 on 2022-04-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='stripe_charge_id',
            new_name='braintree_charge_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ordered',
            new_name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
