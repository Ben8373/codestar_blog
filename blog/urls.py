from django.urls import include, path
from . import views

# In alphabetical order
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit,
        name='comment_edit'
    ),
  path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
