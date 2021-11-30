
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
import json
from usa_app.models import Setting,Post,Video
from usa_app.forms import *
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse
import os
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    context=dict()
    username =  request.POST.get('username')
    password = request.POST.get('password')
    user =authenticate(username=username,password=password)
    if user:
        login(request,user)
        if 'next' in request.POST:
            next =request.POST.get('next')
            return redirect(next)
        else:
            return redirect('homepage')

    return render(request,'registration/login.html',context)
def home_page(request):
    context={}
    project =Setting.objects.filter()
    if project:
        context['project']=project.last()
    return render(request, 'usa_app/index.html',context)

def team_page(request):
    context = {}
    teams = Team.objects.filter()
    context['teams'] = teams
    return render(request, 'usa_app/team.html',context)

def show_file(request):         # To show while click on its icon
    filepath = os.path.join('static', 'sample.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def joinus_create(request):
    form = Joinus_form()
    if request.method == 'POST':
        form = Joinus_form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            messages.add_message(
                request, messages.SUCCESS,'Details have been saved Successfully!!!!')
            return redirect('/joinus')
    return render(request, 'usa_app/joinus_form.html', {'form': form})

def file(request):
    context={}
    files = FileManagement.objects.filter()
    context['files'] = files
    return render(request, 'usa_app/file.html',context)

def video_view(request):
    context = {}
    videos = Video.objects.filter()
    context['videos'] = videos
    return render(request, 'usa_app/videos.html',context)

def delete_video_view(request,id=None):
    context = {}
    video = Video.objects.get(id=id)
    if video:
        video.delete()
        messages.error(request, f'Video Deleted Successfully.')
    return HttpResponse("deleted")

def delete_team_view(request,id=None):
    context = {}
    video = Team.objects.get(id=id)
    if video:
        video.delete()
        messages.error(request, f'Team Deleted Successfully.')
    return HttpResponse("deleted")

def update_video_view(request):
    if 'vupdate_edit' in request.POST:
        print(request.POST)
        id = request.POST.get('id')
        video_link = request.POST.get('video_link')
        try:
            video_link = "https://www.youtube.com/embed/" + video_link.split("?v=")[1]
        except:
            video_link=video_link
        setting=Setting.objects.get(id=id)
        setting.video_link = video_link
        setting.save()
        messages.success(request, f'Video Updated Successfully!')
        return redirect('/')

    if 'vupdate_btn' in request.POST:
        id=request.POST.get('id')
        video_link=request.POST.get('video_link')
        try:
            video_link = "https://www.youtube.com/embed/" + video_link.split("?v=")[1]
        except:
            video_link=video_link
        videos = Video.objects.get(id=id)
        videos.video_link=video_link
        videos.save()
        messages.success(request, f'Video Updated Successfully!')
    return redirect('videos')
def blog_view(request):
    context = {}
    posts = Post.objects.filter().order_by('-id')
    context['posts'] = posts
    return render(request, 'usa_app/blog.html',context)

def post_details_view(request,post_id):
    context = {}
    post = Post.objects.get(pk=post_id)
    realated_post = Post.objects.filter()
    context['post'] = post
    context['realated_post'] = realated_post
    return render(request, 'usa_app/details.html',context)


def team_edit_view(request,team_id):
    context = {}
    team = Team.objects.get(pk=team_id)
    form =TeamForm(request.POST or None, request.FILES or None, instance=team)
    if form.is_valid():
        form.save()
        return HttpResponse("done")
    context['form']=form
    context['id']=team_id
    return render(request, 'usa_app/update.html',context)

def delete_post_view(request,id=None):
    context = {}
    post = Post.objects.get(id=id)
    if post:
        post.delete()
        messages.error(request, f'Post Deleted Successfully.?video={id}')
    return HttpResponse("deleted")

def delete_file_view(request,id=None):
    context = {}
    file = FileManagement.objects.get(id=id)
    if file:
        file.delete()
        messages.error(request, f'File Deleted Successfully.')
    return HttpResponse("deleted")


def update_post_view(request,post_id):
    context = {}
    post = Post.objects.get(pk=post_id)
    form =PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponse("done")
    context['form']=form
    context['id']=post_id
    return render(request, 'usa_app/post_update.html',context)

def update_file_view(request,post_id):
    context = {}
    post = FileManagement.objects.get(pk=post_id)
    form =FileManagementForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponse("done")
    context['form']=form
    context['id']=post_id
    return render(request, 'usa_app/file_update.html',context)


def add_post_view(request):
    context = {}
    form =PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse("done")
    context['form']=form
    return render(request, 'usa_app/add_post.html',context)

def add_team_view(request):
    context = {}
    form =TeamForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse("done")
    context['form']=form
    return render(request, 'usa_app/add_team.html',context)


def add_file_view(request):
    context = {}
    form =FileManagementForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse("done")
    context['form']=form
    return render(request, 'usa_app/add_file.html',context)

def add_video_view(request):
    context = {}
    form =VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse("done")
    context['form']=form
    return render(request, 'usa_app/add_video.html',context)

def setting_view(request):
    context = {}
    setting = Setting.objects.filter(pk=1)
    if setting:
        setting =Setting.objects.filter(pk=1).values(
            'video_link','phone','address','about_company','fb_link'
        )[0]
        context['data']=setting
    return JsonResponse(context)






