from django.db import models

# Create your models here.

class Post(models.Model):
  textmsg = models.CharField(max_length=100)

  def __str__(self):
    return self.textmsg 