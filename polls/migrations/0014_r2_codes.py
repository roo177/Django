# Generated by Django 4.2 on 2023-05-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_delete_r2_codes'),
    ]

    operations = [
        migrations.CreateModel(
            name='r2_codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
