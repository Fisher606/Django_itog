# Generated by Django 4.2.6 on 2023-10-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_category_receipe_category_recipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_recipe',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category_recipe',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Category_Recipe',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
