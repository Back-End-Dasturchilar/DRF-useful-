from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .custompages import CustomPageNumberPagination


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPageNumberPagination


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class InstagramImageList(generics.ListAPIView):
    queryset = InstagramImages.objects.all()
    serializer_class = InstagramImagesSerializer


class AdvertisingList(generics.ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer


class SubscribeList(generics.CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        q = self.request.query_params.get('q')
        cat = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')
        if q:
            return Post.objects.filter(title__icontains=q)
        if cat:
            return Post.objects.filter(category__name__icontains=cat)
        if tag:
            return Post.objects.filter(tags__name__icontains=tag)
        else:
            return Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class HomeView(generics.ListAPIView):
    queryset = Post.objects.all()[:6]
    serializer_class = PostSerializer
