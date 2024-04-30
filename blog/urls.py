from django.urls import path
from blog import views

urlpatterns = [
    path("feautured/", views.PostFeaturedAPIView.as_view()),
    path("popular/", views.PostPopularAPIView.as_view()),
]
