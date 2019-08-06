from django.urls import path,include
from .import views
app_name='predict_entry'
urlpatterns=[
    path('',views.index,name="index"),
]