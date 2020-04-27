from django.db import models
from django.contrib.auth.hashers import make_password
import jdatetime


class Profile(models.Model):

    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Profile, self).save(*args, **kwargs)


class ToDo(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(blank=False, default=jdatetime.date.today())

    def __str__(self):
        return '%s >> %s' % (self.author, self.title)

    class Meta:
        verbose_name_plural = "ToDo Items"
