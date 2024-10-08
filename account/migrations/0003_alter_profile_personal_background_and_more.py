# Generated by Django 5.0.8 on 2024-08-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_personal_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='personal_background',
            field=models.ImageField(blank=True, default='background_default.png', upload_to='users/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='personal_photo',
            field=models.ImageField(blank=True, default='user_default.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]
