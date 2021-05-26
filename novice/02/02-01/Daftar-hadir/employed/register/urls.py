from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employed_form,name='employed_insert'),
    path('<int:id>/', views.employed_form,name='employed_update'),
    path('list/',views.employed_list,name='employed_list')
]