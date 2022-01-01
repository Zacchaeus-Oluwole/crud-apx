from django.urls import path
from api import views

urlpatterns = [
    path('',views.EmployeeList.as_view()),
    
    path('<int:pk>/',views.EmployeeDetail.as_view()),
    # path('update',views.update),
    # path('destroy',views.destroy)
]