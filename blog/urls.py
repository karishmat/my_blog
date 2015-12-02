from django.conf.urls import patterns,include,url
from django.views.generic import ListView,DetailView
from blog.models import Post

urlpatterns = patterns('',

    #url(r'^(?P<pk>\d+)$', DetailView.as_view(
    #    model=Post,
    #    template_name="post.html")),
    url(r'^(?P<pk>\d+)$','blog.views.comment', name="comment"),



    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:10],
        template_name="blog.html")),

    url(r'^archives/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:10],
        template_name="archives.html")),

    url(r'^latestnews/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:5],
        template_name="latestnews.html")),

    url(r'^search/$', 'blog.views.search', name="search"),

    url(r'^signup$', 'blog.views.home', name="home"),

    url(r'^userdata/$', 'blog.views.userdata', name="userdata"),

    url(r'^sendpost/$', 'blog.views.sendpost', name="sendpost"),

    url(r'^like/(?P<postid>\d+)$', 'blog.views.like', name="like"),

)
