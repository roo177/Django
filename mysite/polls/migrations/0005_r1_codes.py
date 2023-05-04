# Generated by Django 4.2 on 2023-05-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_delete_r1_codes'),
    ]

    operations = [
        migrations.CreateModel(
            name='r1_codes',
            fields=[
                ('r_1_code_django', models.CharField(db_column='r_1_code', max_length=50, primary_key=True, serialize=False)),
                ('r_1_desc_en_django', models.CharField(db_column='r_1_desc_en', max_length=50)),
                ('r_1_desc_tr_django', models.CharField(db_column='r_1_desc_tr', max_length=50)),
                ('code_r1_django', models.CharField(db_column='code_r1')),
            ],
            options={
                'db_table': 'r1_code',
                'managed': False,
            },
        ),
    ]
