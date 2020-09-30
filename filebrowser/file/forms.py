from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.forms import ModelForm
# Create your models here.
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Custom_create_folder(ModelForm):
    class Meta:
        model = models.folder_name
        fields = ['title']
class Custom_create_file(ModelForm):
    class Meta:
        model = models.user_file
        fields = ['title','fileupload']
class Custom_create_music(ModelForm):
    class Meta:
        model = models.user_music
        fields = ['title','musicupload']
class Custom_create_pdf(ModelForm):
    class Meta:
        model = models.user_pdf
        fields = ['title','pdfupload']
class Custom_create_image(ModelForm):
    class Meta:
        model = models.user_image
        fields = ['title','imageupload']
class Custom_create_anyfile(ModelForm):
    class Meta:
        model = models.user_anyfile
        fields=['title','anyfileType']                                
class Custom_folder_file(ModelForm):
    class Meta:
        model = models.custom_folder_files
        fields = '__all__'       