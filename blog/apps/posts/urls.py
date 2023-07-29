from django.urls import path
from .views import PostListView, PostDetailView

app_name= 'apps.posts'


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_individual"),
]

# #url de vitas basada en funciones

#from .viws import posts

# urlpatterns = [
#     path('posts/', posts, name='posts'),
# ]
