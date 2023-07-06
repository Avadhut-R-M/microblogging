from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)

    def save(self, *argss, **kwargs) -> None:
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Post, self).save(*argss, **kwargs)


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    like = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "post")
