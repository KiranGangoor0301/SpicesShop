# Generated by Django 5.0.7 on 2024-07-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_feedback_email_remove_feedback_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('veg', 'Vegetarian'), ('nonveg', 'Non-Vegetarian')], max_length=6, null=True),
        ),
    ]