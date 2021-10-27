from django.urls import path
from whatmeet import views
urlpatterns=[
    path("main/",views.main,name='main'),
    path("pro1/",views.pro1,name='pro1')
]