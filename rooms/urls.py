from django.urls import path
from rooms import views

urlpatterns = [
    path('rooms/', views.RoomListView.as_view(), name='room-list'),    
    path('house/<int:pk>', views.HouseDetailView.as_view(), name='house-detail'),    
]