from django.views.generic import ListView, DetailView
from . models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post/post-list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'

