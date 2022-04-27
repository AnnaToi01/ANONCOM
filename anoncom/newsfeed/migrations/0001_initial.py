# Generated by Django 4.0.4 on 2022-04-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_text', models.CharField(max_length=1000)),
                ('post_author', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500)),
                ('comment_author', models.CharField(max_length=50)),
                ('likes', models.IntegerField(default=0)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.allpost')),
            ],
        ),
    ]
