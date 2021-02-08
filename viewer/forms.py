from django.forms import ModelForm
from .models import Course, Lesson, Schedule


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

