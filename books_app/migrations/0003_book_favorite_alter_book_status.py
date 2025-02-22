# Generated by Django 5.1.6 on 2025-02-19 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_book_current_page_book_total_pages_alter_book_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('reading', 'Currently Reading'), ('completed', 'Completed'), ('want to read ', 'Want to Read')], default='wishlist', max_length=20),
        ),
    ]
