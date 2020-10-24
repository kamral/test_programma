from django.urls import path

from .views import  PageDetailView,PageCreateView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('', PageHomeView.as_view(), name='home'),
    # path('new/', views.getdata, name='post_new'),
    path('new/', PageCreateView.as_view(), name='post_new'),
    path('<int:pk>/', PageDetailView.as_view(), name='post_detail')

]