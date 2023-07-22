from django.urls import path
from .import views

urlpatterns = [
    path('ad/', views.addEmployeeView, name='addemployee_url'),
    path('se/', views.showEmployeeView, name='showemployee_url'),
    path('up/<int:pk>/', views.updateEmployeeView, name='updateemployee_url'),
    path('dl/<int:pk>/', views.deleteEmployeeView, name='deleteemployee_url')
]
