from django.urls import path
from .views import BlogListView,DetailblogVIew,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
    path('',BlogListView.as_view(),name = 'home'),
    path('post/<int:pk>/',DetailblogVIew.as_view(), name = 'detailpost'),
    path('create_post/',BlogCreateView.as_view(),name = 'create_post'),
    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name= 'edit_post'),
    path('post/<int:pk>/delete',BlogDeleteView.as_view(), name = 'del_post'),
]