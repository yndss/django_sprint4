from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Category
from django.utils import timezone
from django.conf import settings


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = settings.POSTS_PER_PAGE

    def get_queryset(self):
        qs = Post.objects.select_related(
            'category', 'location', 'author'
        ).all()
        return filter_published_posts(qs)[:5]


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_queryset(self):
        qs = Post.objects.select_related(
            'category', 'location', 'author'
        ).all()
        return filter_published_posts(qs)


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    paginate_by = settings.POSTS_PER_PAGE

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(
            Category,
            slug=category_slug,
            is_published=True
        )
        qs = self.category.posts.select_related(
            'category', 'location', 'author'
        ).all()
        return filter_published_posts(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


def filter_published_posts(queryset):
    return queryset.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
