from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post/post-list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'descricao', 'status']
    template_name = 'post/post-create.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        url = super().form_valid(form)

        return url

class PostUpdateView(UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'descricao', 'status']
    template_name = 'post/post-update.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post-delete.html'
    success_url = reverse_lazy('postList')