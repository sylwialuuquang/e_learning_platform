from django.forms import ModelForm
from .models import Team, Course, Lesson, Schedule, Attachment
from accounts.models import Profile


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Profile.objects.filter(user__groups__name='teacher')


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        exclude = ('course',)

    def __init__(self, *args, **kwargs):
        self.course = Course.objects.filter(id=kwargs.pop('course_pk', None)).first()
        super(LessonForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.course = self.course
        lesson = super(LessonForm, self).save(*args, **kwargs)
        return lesson


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

