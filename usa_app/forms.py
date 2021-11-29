from django import forms
from django.core import validators
from django.forms.widgets import TextInput
from usa_app.models import *
class Joinus_form(forms.ModelForm):
    class Meta:
        model = Joinus
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Fill your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Fill your last name'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Fill your comments'})
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'comment': 'Enter Your Comments',
            'interset': 'Interest',
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model =Team
        fields ='__all__'
    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class VideoForm(forms.ModelForm):
    class Meta:
        model =Video
        fields =['video_link']
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = "Enter " + str(visible.name).title()

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class FileManagementForm(forms.ModelForm):
    class Meta:
        model =FileManagement
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(FileManagementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'