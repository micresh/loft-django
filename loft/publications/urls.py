from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
               path('<int:publication_id>/', views.publication_detail, name='detail'),
               path('<int:publication_id>/comment/', views.comment, name='comment'), ]
