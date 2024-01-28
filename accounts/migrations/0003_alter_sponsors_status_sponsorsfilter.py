# Generated by Django 5.0.1 on 2024-01-28 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_dashboard_sponsors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsors',
            name='status',
            field=models.CharField(choices=[('yangi', 'Yangi'), ('moderatsiyada', 'Moderatsiyada'), ('tasdiqlangan', 'Tasdiqlangan'), ('bekor_qilingan', 'Bekor qilingan')], max_length=20),
        ),
        migrations.CreateModel(
            name='SponsorsFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application_status', models.CharField(choices=[('yangi', 'Yangi'), ('moderatsiyada', 'Moderatsiyada'), ('tasdiqlangan', 'Tasdiqlangan'), ('bekor_qilingan', 'Bekor qilingan')], default='barchasi', max_length=20)),
                ('sponsorship_amount', models.CharField(choices=[('barchasi', 'Barchasi'), ('1_mln', '1 000 000'), ('5_mln', '5 000 000'), ('7_mln', '7 000 000'), ('10_mln', '10 000 000'), ('30_mln', '30 000 000'), ('50_mln', '50 000 000')], default='barchasi', max_length=20)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sponsors')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
