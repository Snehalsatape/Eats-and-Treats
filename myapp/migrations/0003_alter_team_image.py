# Generated by Django 5.0.6 on 2024-05-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_team_alter_contact_options_dish_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='team/'),
        ),
    ]
