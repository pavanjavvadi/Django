from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from filebrowser.utils import unique_slug_generator
from django.db.models import Q



class postmanager(models.Manager):
    def get_queryset(self):
        return post_queryset(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)    

class post_queryset(models.QuerySet):
    def search(self,query=None):
        qs = self
        if query is not None:
            or_lookup = Q(title__icontains=query)
            qs        = qs.filter(or_lookup).distinct()   
        return qs

#create your models here.
class folder_name(models.Model):
    user    = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title   = models.CharField(verbose_name="Folder Name", max_length=100)
    slug    = models.SlugField(max_length=100,null=True,blank=True)

    objects = postmanager()
    
    def __str__(self):
        return self.title

def slug_generator(sender,instance,*args,**kwargs): 
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=folder_name)

class custom_folder_files(models.Model):
    folder         = models.ForeignKey(folder_name,on_delete=models.CASCADE,null=True,blank=True,)
    title          = models.CharField(max_length=100)
    uploaded_files = models.FileField(max_length=100,verbose_name="Upload File",upload_to="others/",default="")

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.uploaded_files.delete()
        super().delete(*args, **kwargs)

class user_file(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title      = models.CharField(max_length=100)
    fileupload = models.FileField(verbose_name="File",max_length=100,upload_to='doc_files/',blank=True,default="",validators=[FileExtensionValidator(allowed_extensions=['doc','docx'],message='Invalid file format, use doc or docx type files')])

    objects    = postmanager()
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.fileupload.delete()
        super().delete(*args, **kwargs)   

class user_music(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title       = models.CharField(max_length=100)
    musicupload = models.FileField(verbose_name="Music",max_length=100,upload_to='music_files/',blank=True,default="",validators=[FileExtensionValidator(allowed_extensions=['mp3','mp4'],message='Invalid file format, use mp3 or mp4 formats')])

    objects     = postmanager()
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.musicupload.delete()
        super().delete(*args, **kwargs)   

class user_pdf(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title     = models.CharField(max_length=100)
    pdfupload = models.FileField(verbose_name="PDF",max_length=100,upload_to='pdf_files/',blank=True,default="",validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='Invalid file format, use pdf format')])

    objects = postmanager()
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdfupload.delete()
        super().delete(*args, **kwargs)   

class user_image(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title       = models.CharField(max_length=100)
    imageupload = models.ImageField(verbose_name="Image",max_length=100,upload_to='image_files/',blank=True,default="",validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'],message='Invalid file format, use jpg, png or jpeg format files')])

    objects = postmanager()

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.imageupload.delete()
        super().delete(*args, **kwargs)   

class user_anyfile(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title       = models.CharField(max_length=100)
    anyfileType = models.FileField(verbose_name="Others",max_length=100,upload_to='any_file_format',blank=True,default="")

    objects     = postmanager()

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.anyfileType.delete()
        super().delete(*args, **kwargs)           