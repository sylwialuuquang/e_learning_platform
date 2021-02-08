from django.urls import path

from .views import TestDetailView


urlpatterns = [
    path('test/<int:pk>', TestDetailView.as_view(), name='test_detail')
]
