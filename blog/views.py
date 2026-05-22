from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
