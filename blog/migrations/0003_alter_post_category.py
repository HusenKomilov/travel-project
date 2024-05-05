# Generated by Django 4.2.7 on 2024-05-05 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_remove_post_tegs_post_author_post_is_featured_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="category", to="blog.category"
            ),
        ),
    ]
