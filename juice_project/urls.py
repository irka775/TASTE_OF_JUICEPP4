from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("about/", include("about.urls")),
    path("summernote/", include("django_summernote.urls")),
    # path('', include('testapp.urls')),
    path('', include('juice_app.urls')),

]
