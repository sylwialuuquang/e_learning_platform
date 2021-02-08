from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ForeignKey, SlugField, DO_NOTHING, CASCADE, TextField, DateTimeField, \
    FileField, IntegerField, TimeField
from accounts.models import Profile
from django.urls import reverse_lazy, reverse


class Team(Model):
    symbol = CharField(max_length=10)
    year_start = CharField(max_length=10)
    supervisor = ForeignKey(Profile, on_delete=DO_NOTHING, related_name='supervisor')

    def __str__(self):
        return self.symbol


class Course(Model):
    name = CharField(max_length=128)
    teacher = ForeignKey(Profile, on_delete=DO_NOTHING)
    team = ForeignKey(Team, on_delete=CASCADE)
    # slug = SlugField()

    def __str__(self):
        return f'{self.name} {self.team}'

    def get_absolute_url(self):
        return reverse_lazy('course_detail', args=[self.id])


class Lesson(Model):
    name = CharField(max_length=128)
    description = TextField()
    course = ForeignKey(Course, on_delete=CASCADE)
    # slug = SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('lesson_detail', args=[self.course.id, self.id])


class Post(Model):
    author = ForeignKey(Profile, on_delete=CASCADE)
    course = ForeignKey(Course, on_delete=CASCADE)
    content = TextField()
    published = DateTimeField()

    def __str__(self):
        return f'{self.author} {self.course}'


class Attachment(Model):
    name = CharField(max_length=128,)
    author = ForeignKey(Profile, on_delete=CASCADE)
    file = FileField(upload_to='files')

    def __str__(self):
        return self.name


class LessonAttachment(Model):
    lesson = ForeignKey(Lesson, on_delete=CASCADE)
    attachment = ForeignKey(Attachment, on_delete=CASCADE, related_name='lesson_attachment')


class PostAttachment(Model):
    post = ForeignKey(Post, on_delete=CASCADE, related_name='post_attachments')
    attachment = ForeignKey(Attachment, on_delete=CASCADE)


class TimeSlot(Model):
    slot_no = IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    time = TimeField()

    def __str__(self):
        return str(self.slot_no)


class Schedule(Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    day_choices = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
    ]
    day = IntegerField(choices=day_choices, default=MONDAY)
    timeslot = ForeignKey(TimeSlot, on_delete=CASCADE, null=True)
    course = ForeignKey(Course, on_delete=CASCADE, null=True)

    def __str__(self):
        return f'{self.day} {self.timeslot.slot_no} {self.course.name}'
