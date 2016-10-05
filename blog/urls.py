from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

# first one is the standard, this shows you can pass view without using views.py, see html file to see how to retreive (I dont really like this way... see booking for my way)
urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                            template_name="blog/blog.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                                         template_name = 'blog/post.html'))]
