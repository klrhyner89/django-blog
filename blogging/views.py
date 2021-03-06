from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.template import loader
from blogging.models import Post, Category

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from blogging.serializers import UserSerializer, PostSerializer, CategorySerializer

# Create your views here.


def stub_view(request, *args, **kwargs):
    body = "Stub View \n\n"
    if args:
        body += "args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):

    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    template_name = "blogging/list.html"


class PostDetailView(DetailView):

    # model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"

    # def get(self, request, *args, **kwargs):
    #     published = Post.objects.exclude(published_date__exact=None)
    #     post = published.get(pk=self.get_object().pk)
    #     context = {'object': post}
    #     return render(request, 'blogging/detail.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint thta allows users to be viewed or edited
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
