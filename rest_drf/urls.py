"""rest_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from drf.views import WomenAPIView
#from drf.views import WomenAPIList, WomenAPIUpdate, WomenAPIDetailView
from drf.views import WomenViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet, basename='women')
#router.register(r'women', WomenViewSet)
#print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("drf.urls")),
    # path('api/v1/womenlist/', WomenAPIView.as_view()),
    # path("api/v1/womenlist/<int:pk>/", WomenAPIView.as_view()),
    #path('api/v1/womenlist/', WomenAPIList.as_view()),
    # path("api/v1/womenlist/<int:pk>/", WomenAPIList.as_view()),
    # path("api/v1/womenlist/<int:pk>/", WomenAPIUpdate.as_view()),
    # path("api/v1/womendetail/<int:pk>/", WomenAPIDetailView.as_view()),

    # path("api/v1/womenlist/", WomenViewSet.as_view({"get":"list"})),
    # path("api/v1/womenlist/<int:pk>/", WomenViewSet.as_view({"put":"update"})),
    path('api/v1/', include(router.urls)),
]
