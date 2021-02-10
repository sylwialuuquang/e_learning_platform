from django.http import HttpResponse
from django.shortcuts import render
import datetime

from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from .models import Team, Course, Lesson, Post, Attachment, Schedule, TimeSlot
from .forms import TeamForm, CourseForm, LessonForm, ScheduleForm
from testsheets.models import Test
from accounts.models import Profile


class TeamDetailView(DetailView):
    model = Team
    context_object_name = 'team'
    template_name = 'team_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(team=self.object)
        context['members'] = Profile.objects.filter(team=self.object)
        context['posts'] = Post.objects.filter(course__team=self.object)
        schedule = Schedule.objects.filter(course__team=self.object).order_by('day').order_by('timeslot__slot_no')
        times_times = TimeSlot.objects.all()
        schedule_table = [
            ['No', 'Time'] + ['Monday', 'Tuesday', 'Wednesady', 'Thursday', 'Friday']
        ]
        for el in times_times:
            schedule_table.append([el.slot_no, el.time] + 5*[''])
        for el in schedule:
            col = el.day + 1
            row = el.timeslot.slot_no
            if col and row:
                schedule_table[row][col] = el.course
        context['schedule'] = schedule_table
        return context


class TeamCreateView(CreateView):
    form_class = TeamForm
    template_name = 'form.html'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object)
        context['posts'] = Post.objects.filter(course=self.object)
        context['tests'] = Test.objects.filter(course=self.object)
        context['schedule'] = Schedule.objects.filter(course=self.object)
        return context


class CourseCreateView(CreateView):
    form_class = CourseForm
    template_name = 'form.html'

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super(CourseCreateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs['teacher'] = self.request.user.profile
    #     return kwargs


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.id})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'delete.html'
    success_url = reverse_lazy('welcome')


class ScheduleCreateView(CreateView):
    form_class = ScheduleForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.course.id})


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'lesson_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context['attachments'] = Attachment.objects.filter(lesson_attachment__lesson=self.object)
        return context


class LessonCreateView(CreateView):
    form_class = LessonForm
    template_name = 'form.html'

    # def get_initial(self, *args, **kwargs):
    #     initial = super(LessonCreateView, self).get_initial(**kwargs)
    #     initial['course'] = self.kwargs['course_pk']
    #     return initial
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(LessonCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['course_pk'] = self.kwargs['course_pk']
        return kwargs


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('lesson_detail', kwargs={'course_pk': self.object.course.id,
                                                     'pk': self.object.id})


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.course.id})


# class AttachmentCreateView(CreateView):
#     form_class = AttachmentForm
#     template_name = 'form.html'

