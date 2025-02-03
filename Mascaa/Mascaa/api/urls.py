from rest_framework.routers import DefaultRouter
from backend.api.urls import User_Router , lib_Admin_Router
from django.urls import path,include

router = DefaultRouter()
#user
router.registry.extend(User_Router.registry)
#admin
router.registry.extend(lib_Admin_Router.registry)

urlpatterns= [ 
    path('', include(router.urls))
]