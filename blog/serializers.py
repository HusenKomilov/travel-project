from rest_framework import serializers
from blog import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("title", "avatar")


class AuthorTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = (
            "title", "avatar", "description", "facebook_link", "twitter_link", "instagram_link", "pinterest_link",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("title",)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = ("title",)


class CategoryCountSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = models.Category
        fields = ("title", "count")


class PostFeauturedSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta:
        model = models.Post
        fields = ("title", "image", "short_content", "published_date", "read_time", "author", "category")


class PostPopularSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta:
        model = models.Post
        fields = ("title", "short_content", "published_date", "read_time", "author", "category")
