from . import views
from django.urls import path

app_name = 'papp'
urlpatterns = [

    path('', views.rac, name='rac'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
