from rest_framework import serializers
from .models import Country, Director, Genre, Movie, Comment

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
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
        fields = '__all__'
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