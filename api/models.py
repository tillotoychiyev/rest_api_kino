from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=50, unique=True,
                validators=[MinLengthValidator(2)], verbose_name="Mamlakat nomi")
    class Meta:
        verbose_name = "Mamlakati"
        verbose_name_plural = "Mamlakatlari"
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True,
                validators=[MinLengthValidator(2)], verbose_name="Janri nomi")

    class Meta:
        verbose_name = "Janri"
        verbose_name_plural = "Janrlari"

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100,
                validators=[MinLengthValidator(2)], verbose_name="Rejissor ismi")
    age = models.IntegerField(verbose_name="Rejissor yoshi",
            validators=[MinValueValidator(20), MaxValueValidator(120)])
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,null=True, blank=True,
            verbose_name="Rejissor yurti")

    class Meta:
        verbose_name = "Rejissori"
        verbose_name_plural = "Rejissorlari"

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=155, validators=[MinLengthValidator(2)],
                             verbose_name="Film nomi")
    description = models.TextField(max_length=500, validators=[MinLengthValidator(20)],
                                   verbose_name="Film haqida")
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900)],
                                   verbose_name="Film premyerasi")
    duration = models.CharField(max_length=50, null=True, blank=True,
                                    verbose_name="Davomiyligi")
    image = models.ImageField(upload_to='images/', null=True, blank=True,
                                    verbose_name="Filmdan suratlar")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name="Rejissor", related_name='movies')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Janri", related_name='movies')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,verbose_name="Mamlakati", related_name='movies')

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=500)
    create = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text