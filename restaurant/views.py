from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework.exceptions import ValidationError
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, DjangoObjectPermissions

# Create your views here.

class IndexView(View):
    def get(self, request):
         return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoObjectPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MenuItemView(generics.ListCreateAPIView):
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [DjangoObjectPermissions]
        return [permission() for permission in permission_classes]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [DjangoObjectPermissions]
        return [permission() for permission in permission_classes]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer