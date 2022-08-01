from django.contrib import admin
from django.urls import path,include
from Dokonapp.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Bu Dokon clani uchun ishlatiladi.",
      contact=openapi.Contact(email="Muhammadali: <Bekruhblog@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()


router.register("suvlar", SuvApiView)
router.register('mijozlar', MijozApiView)
router.register('adminlar', AdminApiView)
router.register('haydovchilar', HaydovchiApiView)
router.register('buyurtmalar', BuyurtmaApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('docs/',schema_view.with_ui('swagger', cache_timeout=0), name='swg_docs'),
]
