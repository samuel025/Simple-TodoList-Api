from django.urls import path
from core import views
urlpatterns = [
    path('', views.Homeview, name='home'),
    path('task-detail/<str:pk>', views.DetailView, name='detail'),
    path('task-create/', views.CreateView, name='create'),
]