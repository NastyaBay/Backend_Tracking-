# Generated by Django 4.2.7 on 2024-04-25 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_forms', '0004_alter_question_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_forms.form'),
        ),
    ]
