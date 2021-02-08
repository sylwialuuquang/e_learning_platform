from django.urls import path
from .views import TeamDetailView, CourseDetailView, CurseCreateView, CourseUpdateView, CourseDeleteView, \
    LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView, ScheduleCreateView


urlpatterns = [
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/create', CurseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/update', CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete', CourseDeleteView.as_view(), name='course_delete'),
    path('course/<int:course_pk>/lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('course/<int:course_pk>/lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('course/<int:course_pk>/lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('course/<int:course_pk>/lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('course/<int:pk>/schedule/update/', ScheduleCreateView.as_view(), name='schedule_create')
]
