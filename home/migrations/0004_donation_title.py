# Generated by Django 4.1.7 on 2023-03-31 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_about_description_alter_about_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation_Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='جزئیات')),
            ],
            options={
                'verbose_name': 'کمک های خیریه',
                'verbose_name_plural': 'کمک های خیریه',
            },
        ),
    ]
