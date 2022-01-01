from django.contrib import admin
from django.urls import path
from crud_app import views

urlpatterns = [
    path('emp',views.emp, name='Welcome'),
    path('show',views.show),
    
    path('edit',views.edit),
    # path('update',views.update),
    # path('destroy',views.destroy)
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]