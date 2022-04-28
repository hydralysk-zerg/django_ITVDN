from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_1/', include('lesson_1.urls')),
    path('lesson_2/', include('lesson_2.urls')),
    path('lesson_3/', include('lesson_3.urls')),
    
]

