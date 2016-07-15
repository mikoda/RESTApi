from Blog.api import views
from django.conf.urls import url, include
from Blog.api.views import (PostListAPIView,
                            PostDetailAPIView,
                            PostUpdateAPIView,
                            PostDeleteAPIView,
                            MyPostAPIView)



urlpatterns = [
    url(r'^post/$', PostListAPIView.as_view(), name='posts'),
    url(r'^post/add/$', views.post_reate_api_view, name='add_post'),
    url(r'^post/my/$', MyPostAPIView.as_view(), name='my_post'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
    url(r'^auth/', include('djoser.urls.authtoken')),
]




