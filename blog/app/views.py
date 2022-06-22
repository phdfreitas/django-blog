from django.views.generic import ListView
from . models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post/list-post.html'

