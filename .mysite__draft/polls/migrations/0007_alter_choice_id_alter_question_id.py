# Generated by Django 4.2 on 2023-05-04 17:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_choice_id_alter_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.UUIDField(default=uuid.UUID('880f506c-ac39-41e7-8251-43fd736baba3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9bc0b909-896c-4d2e-b3d9-f498e6c05de6'), editable=False, primary_key=True, serialize=False),
        ),
    ]
