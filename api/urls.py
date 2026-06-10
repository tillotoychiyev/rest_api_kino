from django.urls import path
from .views import (DirectorAPIView, DirectorRetrieveAPIView,
                    CountryAPIView, CountryRetrieveAPIView,
                    GenreAPIView, GenreRetrieveAPIView,
                    MovieAPIView, MovieRetrieveAPIView,
                    CommentAPIView, CommentRetrieveAPIView)

urlpatterns = [
    path('directors/', DirectorAPIView.as_view()),
    path('directors/<int:pk>/', DirectorRetrieveAPIView.as_view(), name='director_detail'),

    path('countries/', CountryAPIView.as_view()),
    path('countries/<int:pk>/', CountryRetrieveAPIView.as_view(), name='country_detail'),

    path('movies/', MovieAPIView.as_view()),
    path('movies/genre/<int:genre_id>/', MovieAPIView.as_view()),
    path('movies/director/<int:director_id>/', MovieAPIView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveAPIView.as_view(), name='movie_detail'),

    path('genres/', GenreAPIView.as_view()),
    path('genres/<int:pk>/', GenreRetrieveAPIView.as_view(), name='genre_detail'),

    path('movies/<int:movie_id>/comments/', CommentAPIView.as_view()),
    path('movies/<int:movie_id>/comments/<int:comment_id>/', CommentRetrieveAPIView.as_view()),
]