# Generated by Django 4.1.7 on 2023-03-31 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_helpers_options_alter_helpers_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details_Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات بیشتر')),
            ],
            options={
                'verbose_name': 'جزئ کمک',
                'verbose_name_plural': 'جزئیات کمک ها',
            },
        ),
    ]
