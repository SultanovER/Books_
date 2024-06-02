from django.urls import path, include

urlpatterns = [
    path('cloths/', include('cloths.urls')),
]
