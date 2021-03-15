from django.urls import path
from .views import (
    StatusListSearchAPIView,
    StatusAPIView,
    StatusCreateAPIView,
    StatusDetailAPIView,
    StatusUpdateAPIView,
    StatusDeleteAPIView,
    StatusListCreateMixinAPIView,
    StatusDetailUpdateDeleteMixinAPIView,
)


urlpatterns = [
    # path('', StatusListSearchAPIView.as_view()),
    # path('', StatusAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    # path('<int:id>/', StatusDetailAPIView.as_view()),
    # path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
    
    # API View Mixins Urls 
    path('', StatusListCreateMixinAPIView.as_view()),
    path('<int:id>/', StatusDetailUpdateDeleteMixinAPIView.as_view()),
]