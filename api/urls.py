from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

from api import views

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'vaccines', views.VaccineViewSet)
router.register(r'adoption-statuses', views.AdoptionStatusViewSet)
router.register(r'species', views.SpeciesViewSet)
router.register(r'register', views.RegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),
]
