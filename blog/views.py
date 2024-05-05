from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.db.models import Count
# from rest_framework import filters
from blog import models, serializers, paginations


class PostFeaturedAPIView(generics.ListAPIView):
    queryset = models.Post.objects.filter(is_featured=True).order_by("?").select_related("category",
                                                                                         "author").prefetch_related(
        "tags")[:4]
    serializer_class = serializers.PostFeauturedSerializer
    pagination_class = None


class PostPopularAPIView(generics.ListAPIView):
    queryset = models.Post.objects.filter(is_popular=True).order_by("?").select_related("category",
                                                                                        "author").prefetch_related(
        "tags")[:16]
    serializer_class = serializers.PostPopularSerializer
    pagination_class = None


class PostRecentlyAPIView(generics.ListAPIView):
    queryset = models.Post.objects.order_by("?", "-published_date").select_related("category",
                                                                                   "author").prefetch_related("author")
    serializer_class = serializers.PostFeauturedSerializer
    pagination_class = paginations.RecentlyPagination


class TopAuthorAPIView(generics.ListAPIView):
    queryset = models.Author.objects.filter(is_top=True).order_by("?")[:4]
    serializer_class = serializers.AuthorTopSerializer


class CategoryCountAPIView(generics.ListAPIView):
    queryset = models.Category.objects.annotate(count=Count("category"))
    serializer_class = serializers.CategoryCountSerializer


class SearchTagsAPIView(generics.ListAPIView):
    queryset = models.Tags.objects.all()
    serializer_class = serializers.TagsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("tags",)
