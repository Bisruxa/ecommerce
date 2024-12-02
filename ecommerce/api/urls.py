from rest_framework.routers import DefaultRouter
from .views import UserViewSet,ProductViewSet,CatagoryViewSet,OrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'product', ProductViewSet)
router.register(r'catagory',CatagoryViewSet)
router.register(r'orders',OrderViewSet)

urlpatterns = [ 
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
               ] + router.urls