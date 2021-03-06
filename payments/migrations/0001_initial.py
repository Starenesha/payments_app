# Generated by Django 3.0.8 on 2020-07-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(db_index=True, max_length=50, verbose_name='number')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('amount', models.DecimalField(decimal_places=2, default='0.0', max_digits=9, verbose_name='amount')),
                ('purpose_of_payment', models.TextField(max_length=150, verbose_name='purpose of payment')),
                ('status', models.CharField(choices=[(1, 'Waiting'), (2, 'Confirmed'), (3, 'Refunded')], default=1, max_length=10)),
            ],
        ),
    ]
