from django.urls import path
from services import views

urlpatterns = [
    path('services/', views.ServicesList.as_view(), name='services-list'),    
    path('services/<int:pk>', views.ServiceDetail.as_view(), name='service-detail'),    
]