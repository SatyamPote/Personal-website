# PersonalWebsite/backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Backend is running"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),            # Handles GET /
    path('api/', include('api.urls')),  # Replace 'api' with your actual app name if different
]
