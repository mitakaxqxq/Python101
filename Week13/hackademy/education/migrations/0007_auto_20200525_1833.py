# Generated by Django 3.0.6 on 2020-05-25 18:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_auto_20200525_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='url',
            field=models.URLField(),
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('url', models.URLField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Task')),
            ],
        ),
    ]
