# Generated by Django 4.2.3 on 2023-08-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='tms.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='tms.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='tms.company'),
        ),
    ]
