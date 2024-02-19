from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='authors')
    description = models.TextField()
    profession = models.CharField(max_length=212)
    twitter_link = models.URLField()
    github_link = models.URLField()
    facebook_link = models.URLField()
    instagram_link = models.URLField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=212, verbose_name=_("Title"))
    author_name = models.CharField(max_length=212, verbose_name=_("Author Name"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to='posts', verbose_name=_("Image"))
    quotes = models.TextField(verbose_name=_("Quotes"))
    extra_images = models.ImageField(upload_to='images', verbose_name=_("Extra Images"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title


class Subscribe(TimeStampedModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class InstagramImages(TimeStampedModel):
    image = models.ImageField(upload_to='instagram')

    def __str__(self):
        return self.image


class Advertising(TimeStampedModel):
    image = models.ImageField(upload_to='advertising')

    def __str__(self):
        return self.image


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    image = models.ImageField(upload_to='comment_author')
    message = models.TextField()

    def __str__(self):
        return self.name
