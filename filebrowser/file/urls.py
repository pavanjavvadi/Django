from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url

app_name = 'file'
urlpatterns = [

    
    path('',views.login_view,name='login_url'),
    path('register/',views.register_view,name='register_url'),
    path('logout/',views.logout_view,name='logout_url'),
       
    path('home/',views.home_view,name='home_url'),
    path('home/add_folder/',views.add_folder_view,name='create_folder_url'),
    path('home/files/',views.files_view,name='files_url'),
    path('home/files/add_file/',views.add_file_view,name='create_file_url'),
    path('home/music/',views.music_view,name='music_url'),
    path('home/music/add_music/',views.add_music_view,name='create_music_url'),
    path('home/pdf/',views.pdf_view,name='pdf_url'),
    path('home/pdf/add_pdf/',views.add_pdf_view,name='create_pdf_url'),
    path('home/images/',views.images_view,name='images_url'),
    path('home/images/add_images/',views.add_images_view,name='create_images_url'),
    path('home/others/',views.others_view,name='other_file_type_url'),
    path('home/others/add_other_files',views.add_other_files_view,name='create_other_file_type_url'),
    path('home/<int:pk>/<slug:slug_text>/',views.newly_generated_folders_view,name='generated_folders_url'),
    path('home/search/',views.searching_files.as_view(),name='search_url'),
    path('custom_folder_file/',views.create_folder_file,name='custom_folder_file_url'),
   

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="auth/forgot_password.html",success_url="/reset_password_sent/"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="auth/forgot_password_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_form.html",success_url="/reset_password_complete/"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="auth/forgot_password_complete.html"), 
        name="password_reset_complete"),
    
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

    path('delete_file/<int:pk>/',views.delete_file,name="delete_file_url"),
    path('delete_music/<int:pk>/',views.delete_music,name="delete_music_url"),
    path('delete_pdf/<int:pk>/',views.delete_pdf,name="delete_pdf_url"),
    path('delete_image/<int:pk>/',views.delete_image,name="delete_image_url"),
    path('delete_other/<int:pk>/',views.delete_other,name="delete_other_url"),
    path('delete_genarated_files/<int:pk>/',views.delete_generated_folder,name="delete_genarated_files_url"),
    path('delete_folder/<int:pk>/',views.delete_folder,name='delete_folder_url')
    

]

