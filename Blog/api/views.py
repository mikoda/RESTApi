from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Blog.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body')

# @api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated, ))
# def post_collection(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         paginator = Paginator(posts, 10)
#         page = request.query_params.get('page')
#         try:
#             posts = paginator.page(page)
#         except PageNotAnInteger:
#             posts = paginator.page(1)
#         except EmptyPage:
#             posts = paginator.page(paginator.num_pages)
#         serializer = PostListSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         data = {'author': request.user.pk, 'title': request.data.get('title'), 'body': request.data.get('body')}
#         serializer = PostCreateSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def post_reate_api_view(request):
    data = {'author': request.user.pk, 'title': request.data.get('title'), 'body': request.data.get('body')}
    serializer = PostCreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class MyPostAPIView(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_queryset(self):
        """
        This view should return a list of all the posts
        for the currently authenticated user.
        """
        user = self.request.user
        return Post.objects.filter(author=user)