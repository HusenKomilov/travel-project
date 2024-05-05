from django.db import models
from utils.models import BaseModel


class Author(BaseModel):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    content = models.TextField()
    avatar = models.ImageField(upload_to="author")

    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.title


class Tags(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Post(BaseModel):
    title = models.CharField(max_length=256)
    short_content = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to="post")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    tags = models.ManyToManyField(Tags, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")

    read_time = models.IntegerField(default=0)

    published_date = models.DateTimeField(auto_now_add=True)

    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ContactUs(BaseModel):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return self.name


class SubscribeEmail(BaseModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class FAQ(BaseModel):
    title = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return self.title
