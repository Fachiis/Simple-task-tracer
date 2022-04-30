# Generated by Django 4.0.4 on 2022-04-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('U', 'Team User'), ('L', 'Team Leader'), ('M', 'Team Member')], default='U', max_length=1),
        ),
    ]
