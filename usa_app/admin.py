from django.contrib import admin
from .models import Team,Joinus,Post,Video,Setting,FileManagement
# Register your models here.
from django.utils.html import format_html

class JoinusAdmin(admin.ModelAdmin):
    pass
    # list_display=['id','fno','fname','fage','faddr']

admin.site.register(Joinus, JoinusAdmin)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['name','position','created_at','status']
    list_filter = ['status']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display=['videos_link','video_link','video_text','created_at','status']
    list_filter = ['status']
    def videos_link(self, obj):
        return format_html(f'''
                    <div class="text-bold"> videos link {obj.id}</div>
                    ''')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['photo','title','created_at','status']
    list_filter = ['status','created_at']
    def photo(self, obj):
        return format_html(f'''
                    <img src="/media/{obj.image}" alt="/{obj.image}" width="50px" height="50" style="border-radius:50%">
                    ''')


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display=['video_link','created_at']
    list_filter = ['created_at']

@admin.register(FileManagement)
class FileManagementAdmin(admin.ModelAdmin):
    list_display=['file_type','file','created_at']
    list_filter = ['created_at']
