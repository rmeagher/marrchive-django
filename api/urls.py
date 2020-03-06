from django.urls import include, path
# from rest_framework import routers
from api import views
from rest_framework_nested import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'books/?', views.BookViewSet)
router.register(r'authors/?', views.AuthorViewSet)

books_router = routers.NestedDefaultRouter(router, r'books/?', lookup='book')
books_router.register(r'authors/?', views.AuthorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
apiurlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(books_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]