# Generated by Django 4.2 on 2023-05-04 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_r1code_r2code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='R1Code',
        ),
        migrations.DeleteModel(
            name='R2Code',
        ),
    ]
