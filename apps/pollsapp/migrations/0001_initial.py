# Generated by Django 4.2 on 2023-05-09 15:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('7c0817b3-9562-45c6-8175-11fed8771fd7'), editable=False, primary_key=True, serialize=False)),
                ('hashed_id', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('4ef617ac-82b1-469b-ab23-25ad1b1c5494'), editable=False, primary_key=True, serialize=False)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollsapp.question')),
            ],
        ),
    ]