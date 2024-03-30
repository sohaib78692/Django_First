from django.urls import path
from . import views

urlpatterns=[
    path("blogposts/<int:pk>/",
         views.BlogPostRUD.as_view(),
         name="update"),
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
]