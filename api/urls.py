from django.urls import path
from .views import (DirectorAPIView, DirectorRetrieveAPIView,
                    CountryAPIView, CountryRetrieveAPIView,
                    GenreAPIView, GenreRetrieveAPIView,
                    MovieAPIView, MovieRetrieveAPIView,
                    CommentAPIView, CommentRetrieveAPIView)

urlpatterns = [
    path('directors/', DirectorAPIView.as_view()),
    path('directors/<int:pk>/', DirectorRetrieveAPIView.as_view()),

    path('countries/', CountryAPIView.as_view()),
    path('countries/<int:pk>/', CountryRetrieveAPIView.as_view()),

    path('movies/', MovieAPIView.as_view()),
    path('movies/genre/<int:genre_id>/', MovieAPIView.as_view()),
    path('movies/director/<int:director_id>/', MovieAPIView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveAPIView.as_view()),

    path('genres/', GenreAPIView.as_view()),
    path('genres/<int:pk>/', GenreRetrieveAPIView.as_view()),

    path('movies/<int:movie_id>/comments/', CommentAPIView.as_view()),
    path('movies/<int:movie_id>/comments/<int:comment_id>/', CommentRetrieveAPIView.as_view()),
]