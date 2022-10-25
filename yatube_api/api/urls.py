from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)
from django.urls import include, path
from rest_framework import routers

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet)


router_v1 = routers.DefaultRouter()
router_v1.register('groups', GroupViewSet)
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('follow', FollowViewSet, basename='followers')


jwt_patterns = [
    path(
        'jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'jwt/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    )
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include(jwt_patterns)),
]
