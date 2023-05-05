# Generated by Django 4.2 on 2023-05-04 10:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_choice_id_alter_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d5be5784-d728-4de9-9900-33d44ea55727'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1f8baac5-9548-443f-81ae-1847c6da4113'), editable=False, primary_key=True, serialize=False),
        ),
    ]
