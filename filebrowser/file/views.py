from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.urls import reverse
from . import forms
from django.contrib import messages
from django.conf import settings
from . import models
import os
from itertools import chain
from django.views.generic import ListView

# Create your views here.
#login
def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('file:home_url'))
        else:
            messages.info(request,"Invalid Username or Password")    
            return render(request,'auth/login.html',context)

    else:
        return render(request,'auth/login.html',context)
#register
def register_view(request):
    context = {}   
    if request.method == 'POST':
        form = forms.CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('file:login_url')
    else:
        form    = forms.CustomUserForm()
        context = {'form': form}
        return render(request,'auth/register.html',context)        

#logout
@login_required(login_url="file:login_url")
def logout_view(request):
    logout(request)
    return redirect('file:login_url')        


#home 
@login_required(login_url="file:login_url")
def home_view(request):
    context = {'form': models.folder_name.objects.all(),'create_folder': True,}
    return render(request,'file/home.html',context) 
#add folder
@login_required(login_url="file:login_url")
def add_folder_view(request):
    if request.method == 'POST':
        form = forms.Custom_create_folder(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file:home_url')
    else:
        context = {'form': forms.Custom_create_folder()}
        return render(request, 'file/create_folder.html',context)


#view files
@login_required(login_url="file:login_url")
def files_view(request):
    context = {'form': models.user_file.objects.all(),'type': 'File'}
    return render(request,'file/files.html',context)
#add files
@login_required(login_url="file:login_url")
def add_file_view(request):
    if request.method == 'POST':
        form = forms.Custom_create_file(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file:files_url')    
    else:
        context = {'form':forms.Custom_create_file()}
        return render(request, 'file/create_file.html',context)


#view music files
@login_required(login_url="file:login_url")
def music_view(request):
    context = {'form':models.user_music.objects.all(),'type':'Music'}
    return render(request, 'file/files.html',context)
#add music files
@login_required(login_url="file:login_url")
def add_music_view(request):
    if request.method == 'POST':
        form = forms.Custom_create_music(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file:music_url')    
    else:
        context = {'form':forms.Custom_create_music()}
        return render(request, 'file/create_file.html',context)


#view pdf files
@login_required(login_url="file:login_url")
def pdf_view(request):
    context = {'form': models.user_pdf.objects.all(),'type':'PDF'}
    return render(request,'file/files.html',context)
#add pdf files
@login_required(login_url="file:login_url")
def add_pdf_view(request):
    if request.method == 'POST':
        form = forms.Custom_create_pdf(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file:pdf_url')    
    else:
        context = {'form':forms.Custom_create_pdf()}
        return render(request, 'file/create_file.html',context)


#view images
@login_required(login_url="file:login_url")
def images_view(request):
    context = {'form': models.user_image.objects.all(),'type':'Images'}
    return render(request,'file/files.html', context)
#add images
@login_required(login_url="file:login_url")
def add_images_view(request):
    if request.method == 'POST':
        form = forms.Custom_create_image(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file:images_url')    
    else:
        context = {'form':forms.Custom_create_image()}
        return render(request, 'file/create_file.html',context)



#view other files
@login_required(login_url="file:login_url")
def others_view(request):
    context = {'form': models.user_anyfile.objects.all(),'type':'Others'}
    return render(request, 'file/files.html',context)
#add others
@login_required(login_url="file:login_url")
def add_other_files_view(request):
    if request.method == 'POST':
        form = forms.Custom_create_anyfile(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file:other_file_type_url')    
    else:
        context = {'form':forms.Custom_create_anyfile()}
        return render(request, 'file/create_file.html',context)

@login_required(login_url="file:login_url")
def newly_generated_folders_view(request,slug_text):
    q    = models.folder_name.objects.filter(slug = slug_text)
    form = models.custom_folder_files.objects.filter(folder = slug_text)
    a    = slug_text
    context = {'type':a,'form':form}
    if q.exists():
        return render(request,'file/files.html',context)
    else:
        return HttpResponse("failed to render correct folder")

@login_required(login_url="file:login_url")
def create_folder_file(request):
    slug_text = slug_text
    if request.method == 'POST':
        form = forms.Custom_folder_file(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file:home_url')
    else:
        context = {'form':forms.Custom_folder_file()}
        return render(request,'file/create_file.html',context)

#download file
@login_required(login_url="file:login_url")
def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)    
    if os.path.exists(file_path):
        with open(file_path,'rb') as f:
            response                        =  HttpResponse(f.read())
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response

    raise Http404



@login_required(login_url="file:login_url")
class Search_View(ListView):
    template_name = 'file/search.html'
    paginate_by = 20
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        
        if query is not None:
            folder_results    = models.folder_name.objects.search(query)
            file_results      = models.user_file.objects.search(query)
            music_results     = models.user_music.objects.search(query)
            pdf_results       = models.user_pdf.objects.search(query)
            image_results     = models.user_image.objects.search(query)
            anyfile_results   = models.user_anyfile.objects.search(query)
            
            # combine querysets 
            queryset_chain = chain( folder_results,file_results,music_results,pdf_results,image_results,anyfile_results )       
            qs = sorted(queryset_chain,key=lambda instance: instance.pk,reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return models.folder_name.objects.none() # just an empty queryset as default


       #delete files
@login_required(login_url="file:login_url")
def delete_file(request,pk):
    deleting_file = models.user_file.object.get(pk=pk)
    deleting_file.delete()
    return redirect("file:files_url")

@login_required(login_url="file:login_url")
def delete_file(request,pk):
    deleting_file = models.user_music.object.get(pk=pk)
    deleting_file.delete()
    return redirect("file:music_url")

@login_required(login_url="file:login_url")
def delete_file(request,pk):
    deleting_file = models.user_pdf.object.get(pk=pk)
    deleting_file.delete()
    return redirect("file:pdf_url")

@login_required(login_url="file:login_url")
def delete_file(request,pk):
    deleting_file = models.user_image.object.get(pk=pk)
    deleting_file.delete()
    return redirect("file:images_url")

@login_required(login_url="file:login_url")
def delete_file(request,pk):
    deleting_file = models.user_anyfile.object.get(pk=pk)
    deleting_file.delete()
    return redirect("file:other_file_type_url")                
