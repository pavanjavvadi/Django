from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.folder_name)
admin.site.register(models.user_file)
admin.site.register(models.user_music)
admin.site.register(models.user_pdf)
admin.site.register(models.user_image)
admin.site.register(models.user_anyfile)
admin.site.register(models.custom_folder_files)