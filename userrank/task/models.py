from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=20)
    user_rank = models.IntegerField(default=0)
    user_id = models.CharField(max_length=15) 

    def __str__(self):
        return self.username
    

class TweetModel(models.Model):
    content = models.TextField()
    mentioned_users = models.ManyToManyField(UserModel, related_name='mentioned_in_tweets')

    def __str__(self):
        return self.content
    
class TaskModel(models.Model):

    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def str(self):
        return self.task_name

    