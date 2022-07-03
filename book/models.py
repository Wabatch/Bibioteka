from email.policy import default
from django.db import models

# Create your models here.

from time import timezone
from xmlrpc.client import DateTime
from django.db import models
from django.forms import DateTimeField

from users.models import Users


from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    softCover = "Miękka"
    hardCover = "Twarda"
    typeOfBookCover = [
        (softCover, "Miękka"),
        (hardCover, "Twarda"),
    ]
    title = models.TextField()
    author = models.TextField()
    cover = models.CharField(
        default=softCover,
        null=False,
        blank=False,
        max_length=6,
        choices=typeOfBookCover,
    )
    publisher = models.TextField()
    dateOfRelease = models.DateField()
    dateOfPublishing = models.DateField(default=None, null=True, blank=True)
    amountOfPages = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    image = models.ImageField(blank=True, default='default.jpg')

    def __str__(self) -> str:
        return self.title