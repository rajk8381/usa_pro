from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home_page,name='homepage'),
    path('login/', views.login_view,name='login'),
    path('team/', views.team_page,name='teampage'),
    path('file/', views.show_file,name='pdf'),
    path('joinus/', views.joinus_create,name='joinform'),
    path('files/', views.file, name="file2"),
    path('videos/', views.video_view, name="videos"),
    path('video/delete/<id>', views.delete_video_view, name="videos_delete"),
    path('team/delete/<id>', views.delete_team_view, name="team_delete"),
    path('post/delete/<id>', views.delete_post_view, name="post_delete"),
    path('file/delete/<id>', views.delete_file_view, name="file_delete"),
    path('video/update/', views.update_video_view, name="videos_update"),
    path('blog/', views.blog_view, name="blog"),
    path('load/setting/', views.setting_view, name="setting"),
    path('details/<post_id>/', views.post_details_view, name="details"),
    path('team/update/<team_id>/', views.team_edit_view, name="team_update"),
    path('post/update/<post_id>/', views.update_post_view, name="post_update"),
    path('file/update/<post_id>/', views.update_file_view, name="file_update"),
    path('video/add/', views.add_post_view, name="add_update"),

]
