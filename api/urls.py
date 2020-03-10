from django.urls import include, path
from django.views.generic import RedirectView
# from rest_framework import routers

from api import views
from rest_framework_nested import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'books/?', views.BookViewSet)
router.register(r'authors/?', views.AuthorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
api_url_patterns = [
    path('', RedirectView.as_view(url='api/v1/', permanent=False)),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# DJA needs to create defaultRouter patterns for these
book_url_patterns = [
    path('api/v1/books/<pk>/<related_field>', views.BookViewSet.as_view({'get': 'retrieve_related'}),
         name='book-related'),
    path('api/v1/books/<pk>/relationships/<related_field>', views.BookRelationshipView.as_view(),
         name='book-relationships'),
]

author_url_patterns = [
    path('api/v1/authors/<pk>/<related_field>', views.AuthorViewSet.as_view({'get': 'retrieve_related'}),
         name='author-related'),
    path('api/v1/authors/<pk>/relationships/<related_field>', views.AuthorRelationshipView.as_view(),
         name='author-relationships'),
]

api_url_patterns += book_url_patterns + author_url_patterns
