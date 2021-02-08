from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, DO_NOTHING, CASCADE, BooleanField

from viewer.models import Course, Attachment


class Test(Model):
    title = CharField(max_length=128)
    description = TextField()
    course = ForeignKey(Course, on_delete=DO_NOTHING)

    def __str__(self):
        return self.title


class TestAttachment(Model):
    test = ForeignKey(Test, on_delete=CASCADE)
    attachment = ForeignKey(Attachment, on_delete=CASCADE)


class TestQuestion(Model):
    type_choices = [
        ('closed', 'closed'),
        ('wh', 'wh')
    ]
    test = ForeignKey(Test, on_delete=CASCADE)
    type = CharField(max_length=6, default='closed', choices=type_choices)
    question = TextField()
    attachment = ForeignKey(TestAttachment, on_delete=DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.question[:128]


class TestAnswer(Model):
    question = ForeignKey(TestQuestion, on_delete=CASCADE, related_name='test_answer')
    answer = CharField(max_length=512)
    correct = BooleanField()

    def __str__(self):
        return self.answer

