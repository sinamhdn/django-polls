# Generated by Django 4.2 on 2023-05-05 07:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_choice_id_alter_question_hashed_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.UUIDField(default=uuid.UUID('45a7730a-b747-408d-88a7-0b7f22068ff8'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b449919a-f314-42fb-b417-eabc213d0dd3'), editable=False, primary_key=True, serialize=False),
        ),
    ]