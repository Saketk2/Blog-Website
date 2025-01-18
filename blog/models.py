from django.db import models

# Create your models here.
class BlogPost(models.Model):
    author = models.CharField(max_length = 200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return self.content[:50]
