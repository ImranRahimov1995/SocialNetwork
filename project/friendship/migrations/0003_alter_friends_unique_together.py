# Generated by Django 3.2.9 on 2021-11-22 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_friends'),
        ('friendship', '0002_auto_20211122_1134'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together={('user1', 'user2')},
        ),
    ]
