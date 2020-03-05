from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'books/?', views.BookViewSet)
router.register(r'authors/?', views.AuthorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
apiurlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]