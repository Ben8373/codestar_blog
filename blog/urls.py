from django.urls import include, path
from . import views

# In alphabetical order
urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
