from django.urls import path
from . import views
from .views import IndexView

# url paths list
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]