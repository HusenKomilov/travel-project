from django.urls import path
from blog import views

urlpatterns = [
    path("feautured/", views.PostFeaturedAPIView.as_view()),
    path("popular/", views.PostPopularAPIView.as_view()),
    path("recently/", views.PostRecentlyAPIView.as_view()),
    path("top-author/", views.TopAuthorAPIView.as_view()),
    path("category-count/", views.CategoryCountAPIView.as_view()),
    path("search-post/", views.SearchTagsAPIView.as_view()),
]
