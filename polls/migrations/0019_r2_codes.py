# Generated by Django 4.2 on 2023-05-04 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20230504_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='r2_codes',
            fields=[
                ('r_1_code_django', models.CharField(db_column='r_1_code', max_length=2)),
                ('r_2_code_django', models.CharField(db_column='r_2_code', max_length=2)),
                ('r_2_desc_en_django', models.CharField(db_column='r_2_desc_en', max_length=150)),
                ('r_2_desc_tr_django', models.CharField(db_column='r_2_desc_tr', max_length=150)),
            ],
            options={
                'db_table': 'r2_code',
                'managed': False,
            },
        ),
    ]
