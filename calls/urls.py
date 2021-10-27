
from django.urls import path
from calls import views

urlpatterns=[
    path('sample/',views.sample,name="sample"),
    path('parent/',views.parent,name="parent"),
    path('child/',views.child,name="child"),
]