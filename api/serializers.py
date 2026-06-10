from rest_framework import serializers
from .models import Country, Director, Genre, Movie, Comment


class MovieSerializerForCountry(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['country']

class CountrySerializer(serializers.ModelSerializer):
    # movies = serializers.StringRelatedField(many=True)
    # movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie_detail')
    # movies = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # url = serializers.HyperlinkedIdentityField(view_name='country_detail')
    movies = MovieSerializerForCountry(many=True)
    class Meta:
        model = Country
        fields = '__all__'

    def create(self, validated_data):
        movies = validated_data.pop('movies')
        country = Country.objects.create(**validated_data)
        movie_list = []

        for movie in movies:
            movie_list.append(
                Movie(country=country, **movie)
            )

        Movie.objects.bulk_create(movie_list)
        return country

    def update(self, instance, validated_data):
        movies = validated_data.pop('movies', [])
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for movie in movies:
            Movie.objects.create(
                country=instance,
                **movie
            )
        return instance

class DirectorSerializer(serializers.ModelSerializer):
    # movies = serializers.StringRelatedField(many=True)
    # movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='director_detail')
    movies = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
#     url = serializers.HyperlinkedIdentityField(view_name='country_detail')
#     movies = MovieSerializerForCountry(many=True)
    class Meta:
        model = Director
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    # movies = serializers.StringRelatedField(many=True)
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='genre_detail')
    # movies = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
#     url = serializers.HyperlinkedIdentityField(view_name='country_detail')
#     movies = MovieSerializerForCountry(many=True)
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genre_write = serializers.ChoiceField(
        choices=Genre.objects.all(),
        write_only=True
    )
    class Meta:
        model = Movie
        exclude = ['country']
        depth = 1

    def create(self, validated_data):
        genre_write = validated_data.pop("genre_write")
        movie = Movie.objects.create(genre=genre_write, **validated_data)
        movie.save()
        return movie

    def update(self, instance, validated_data):
        instance.genre = validated_data.pop("genre_write") or instance.genre
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['image']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text', 'create']