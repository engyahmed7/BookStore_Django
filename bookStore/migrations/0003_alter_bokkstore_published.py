# Generated by Django 4.2.11 on 2024-05-07 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookStore', '0002_alter_bokkstore_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bokkstore',
            name='published',
            field=models.DateField(),
        ),
    ]
