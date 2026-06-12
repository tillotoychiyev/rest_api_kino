from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .serializers import DirectorSerializer, MovieSerializer, GenreSerializer, CountrySerializer, UserSerializer, CommentSerializer
from .models import Movie, Genre, Director, Country, Comment
from .permissions import MyIsAuthenticatedOrReadOnly, CommentAuthorPermission

class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class MovieAPIViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class DirectorAPIViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class GenreAPIViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class CommentAPIViewSet(MovieAPIViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        MyIsAuthenticatedOrReadOnly,CommentAuthorPermission
    ]
    lookup_url_kwarg = 'comment_id'
    def get_queryset(self):
        return Comment.objects.filter(movie_id=self.kwargs.get('movie_id'))

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_id'))
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['movie'] = movie
        serializer.save()
        return serializer














#
# class CountryAPIView(ListCreateAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer
#
# class CountryRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer


# class DirectorAPIView(ListCreateAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer
#
# class DirectorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer


#
# class MovieAPIView(ListCreateAPIView):
#     serializer_class = MovieSerializer
#     permission_classes = [MyIsAuthenticatedOrReadOnly]
#     def get_queryset(self):
#         genre_id = self.kwargs.get("genre_id")
#         director_id = self.kwargs.get("director_id")
#         if genre_id:
#             return Movie.objects.filter(genre_id=genre_id)
#         if director_id:
#             return Movie.objects.filter(director_id=director_id)
#         return Movie.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.user.is_staff:
#             return MovieSerializer
#         return UserSerializer
#
# class MovieRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [MyIsAuthenticatedOrReadOnly]
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class GenreAPIView(ListCreateAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#
# class GenreRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#
# class CommentAPIView(ListCreateAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [MyIsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         return Comment.objects.filter(movie_id=self.kwargs.get('movie_id'))
#
#     def perform_create(self, serializer):
#         movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_id'))
#         serializer.user = self.request.user
#         serializer.validated_data['user'] = self.request.user
#         serializer.validated_data['movie'] = movie
#         serializer.save()
#         return self
#
# class CommentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [MyIsAuthenticatedOrReadOnly, CommentAuthorPermission]
#     lookup_url_kwarg = 'comment_id'