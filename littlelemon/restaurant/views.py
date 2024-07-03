from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Menu, MenuItem, Booking

from .serializers import MenuSerializer, MenuItemSerializer, BookingSerializer, UserSerializer

from django.contrib.auth.models import User


# Create your views here.

# def sayHello(request):
#  return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuItemView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

#class MenuItemView(generics.ListCreateAPIView):
#    queryset = Menu.objects.all()
#    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




@api_view()
@permission_classes([IsAuthenticated])

# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})