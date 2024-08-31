from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CreatingSecond.views import CurrentTimeViewSet 

router = DefaultRouter()
router.register(r'time', CurrentTimeViewSet) 

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
