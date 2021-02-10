from django.urls import path

from .views import TestDetailView, create_test


urlpatterns = [
    path('test/<int:pk>', TestDetailView.as_view(), name='test_detail'),
    path('test/create', create_test, name='test_create')
]
