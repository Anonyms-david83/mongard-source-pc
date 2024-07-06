# Generated by Django 5.0.6 on 2024-06-17 11:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_comment_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pvotes', to='home.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uvote', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
