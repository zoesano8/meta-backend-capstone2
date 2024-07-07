from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuView, MenuItemView, SingleMenuItemView

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
router.register(r'menus', MenuView, basename='menu')
router.register(r'menuitems', MenuItemView, basename='menuitem')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('message/', views.msg, name='message'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),  # Include the router URLs
]
