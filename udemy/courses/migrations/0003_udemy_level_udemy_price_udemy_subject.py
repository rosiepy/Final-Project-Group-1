# Generated by Django 4.2.3 on 2023-07-28 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_alter_level_options_alter_price_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="udemy",
            name="level",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="courses.level",
            ),
        ),
        migrations.AddField(
            model_name="udemy",
            name="price",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="courses.price",
            ),
        ),
        migrations.AddField(
            model_name="udemy",
            name="subject",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="courses.subjects",
            ),
        ),
    ]
