from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path
from .views import SubmitLoginView, SubmitPasswordChangeView


urlpatterns = [
    path('login/', SubmitLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', SubmitPasswordChangeView.as_view(), name='password_change'),
    # path('password-reset/', PasswordResetView.as_view(template_name='form.html'), name='password_reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(template_name='form.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='form.html'), name='password_reset_confirm'),
    # path('reset/done', PasswordResetCompleteView.as_view(template_name='form.html'), name='password_reset_complete')
]
