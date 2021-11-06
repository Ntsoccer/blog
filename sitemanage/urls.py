from django.urls import path, include

app_name = 'sitemanage'

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
