# Generated by Django 4.2.3 on 2023-07-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_member_address_member_course_member_document_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
