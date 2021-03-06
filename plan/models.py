from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django_resized import ResizedImageField


class Profile(models.Model):

    username = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    #avatar = models.ImageField(upload_to='avatars', blank=True)
    avatar = ResizedImageField(
        size=[500, 500], crop=['middle', 'center'], upload_to='avatars', blank=True, null=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)


class ToDo(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = jmodels.jDateTimeField(auto_now=True, blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.author, self.title)

    class Meta:
        verbose_name_plural = "ToDo Items"


LANGUAGES = [
    ('fa', 'Persian'),
    ('en', 'English'),
]

THEMES = [
    ('blue', 'Blue'),
    ('pink', 'Pink'),
    ('yellow', 'Yellow'),
]


class Theme(models.Model):

    username = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    language = models.CharField(choices=LANGUAGES, max_length=50, default='fa')
    theme = models.CharField(choices=THEMES, max_length=50, default='blue')

    def __str__(self):
        return str(self.username)
