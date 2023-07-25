from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'booking/tables', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]