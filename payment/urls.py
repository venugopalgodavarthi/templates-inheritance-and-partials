from django.urls import path
from payment import views
urlpatterns=[
    path('parent/',views.parent,name='parent'),
    path('child/',views.child,name='child'),
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index'),
]
