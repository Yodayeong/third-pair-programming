from django.db import models

# Create your models here.
class Board(models.Model):
    boards = models.CharField(max_length=15)
    user = models.CharField(max_length=15)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)