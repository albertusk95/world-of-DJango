from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'album/', views.index, name="index")
]
