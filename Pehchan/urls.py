from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.Home_view, name='home'),
    path("profile/", views.profile_view, name="profile"),
    path("profile/update/", views.create_or_update_profile, name="profile_update"),
    path("profile/delete/", views.delete_profile, name="delete_profile"),
    path("feed/", views.feed_view, name="feed"),
    path("post/", views.create_post_view, name="post"),
    path("post/update/<int:pk>/", views.update_post, name="post_update"),
    path("post/delete/<int:pk>/", views.delete_post, name="post_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
