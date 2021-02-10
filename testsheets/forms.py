from django.forms import ModelForm
from .models import Test, TestAttachment, TestQuestion, TestAnswer


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


# class TestAttachmentForm(ModelForm):
#     class Meta:
#         model = TestAttachment
#         fields = '__all__'


class TestQuestionForm(ModelForm):
    class Meta:
        model = TestQuestion
        fields = ('type', 'question')


class TestAnswerForm(ModelForm):
    class Meta:
        model = TestAnswer
        fields = ('answer', 'correct')
