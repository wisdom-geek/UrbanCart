# Generated by Django 5.0.7 on 2024-07-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_cid_alter_vendor_vid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitems',
            name='invoice_no',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]