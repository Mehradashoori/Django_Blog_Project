from django.urls import path
from . import views

urlpatterns = [
    # Class Based View
    path('', views.PostListView.as_view(), name='posts_lists'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='posts_detail'),
    path('add/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete')
]
