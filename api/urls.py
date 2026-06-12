from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (DirectorAPIViewSet,
                    CountryAPIViewSet,
                    GenreAPIViewSet,
                    MovieAPIViewSet,
                    CommentAPIViewSet)

router = SimpleRouter()
router.register('countries', CountryAPIViewSet)
router.register('movies', MovieAPIViewSet)
router.register('directors', DirectorAPIViewSet)
router.register('genres', GenreAPIViewSet)

urlpatterns = [
    path('movies/<int:movie_id>/comments/',
    CommentAPIViewSet.as_view({'get':'list', 'post':'create'}), name='comment_list'),

    path('movies/<int:movie_id>/comments/<int:comment_id>/',
    CommentAPIViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='comment_detail'),
    path('', include(router.urls))
]