from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]