# Generated by Django 4.2 on 2023-05-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0002_rename_email_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
