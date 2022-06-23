from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='postList'),
    path('newpost', views.PostCreateView.as_view(), name='postCreate'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='postDetail'),
    path('edit/<slug:slug>', views.PostUpdateView.as_view(), name='postUpdate'),
    path('delete/<slug:slug>', views.PostDeleteView.as_view(), name='postDelete'),
]