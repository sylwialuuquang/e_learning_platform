"""e_learning_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.models import Profile
from django.views.generic import TemplateView
from viewer.models import Team, Course, Lesson, Post, Attachment, LessonAttachment, PostAttachment, TimeSlot, Schedule
from testsheets.models import Test, TestAttachment, TestQuestion, TestAnswer

admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Post)
admin.site.register(Attachment)
admin.site.register(LessonAttachment)
admin.site.register(PostAttachment)
admin.site.register(TimeSlot)
admin.site.register(Schedule)
admin.site.register(Test)
admin.site.register(TestAttachment)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('viewer/', include('viewer.urls')),
    path('accounts/', include('accounts.urls')),
    path('testsheet/', include('testsheets.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
