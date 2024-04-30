from rest_framework import generics
from blog import models, serializers


class PostFeaturedAPIView(generics.ListAPIView):
    queryset = models.Post.objects.filter(is_featured=True).order_by("?")[:4]
    serializer_class = serializers.PostFeauturedSerializer
    pagination_class = None


class PostPopularAPIView(generics.ListAPIView):
    queryset = models.Post.objects.filter(is_popular=True).order_by("?")[:8]
    print(queryset)
    serializer_class = serializers.PostPopularSerializer
    pagination_class = None
