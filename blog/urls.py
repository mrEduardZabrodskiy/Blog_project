from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/<int:pk>', views.profile_view, name='profile_view'),
    path('post_delete/<int:pk>', views.post_delete, name='post_delete'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)