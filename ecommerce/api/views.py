from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,ProductSerializer,CatagorySerializer,OrderSerializer
from .permissions import CustomPermission
User = get_user_model()
from products.models import Product,Catagory
from orders.models import Order
from rest_framework.permissions import IsAuthenticated

class UserViewSet(ReadOnlyModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class ProductViewSet(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes=[IsAuthenticated,CustomPermission]
class CatagoryViewSet(ModelViewSet):
  queryset = Catagory.objects.all()
  serializer_class = CatagorySerializer
class OrderViewSet(ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer