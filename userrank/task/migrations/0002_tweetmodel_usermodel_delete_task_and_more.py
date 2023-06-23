# Generated by Django 4.2.2 on 2023-06-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('user_rank', models.IntegerField(default=0)),
                ('user_id', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='tweetmodel',
            name='mentioned_users',
            field=models.ManyToManyField(related_name='mentioned_in_tweets', to='task.usermodel'),
        ),
    ]