# Generated by Django 4.1.13 on 2024-08-17 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0004_alter_action_target_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_object', to='contenttypes.contenttype'),
        ),
    ]
