from .models import Movie, Genre, Director, Country
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DirectorSerializer, MovieSerializer, GenreSerializer, CountrySerializer, UserSerializer

class CountryAPIView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DirectorAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    def get_queryset(self):
        genre_id = self.kwargs.get("genre_id")
        director_id = self.kwargs.get("director_id")
        if genre_id:
            return Movie.objects.filter(genre_id=genre_id)
        if director_id:
            return Movie.objects.filter(director_id=director_id)
        return Movie.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MovieSerializer
        return UserSerializer

class MovieRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer