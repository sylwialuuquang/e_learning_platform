from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from .models import Test, TestQuestion
from .forms import TestForm, TestQuestionForm, TestAnswerForm


class TestDetailView(DetailView):
    model = Test
    context_object_name = 'test'
    template_name = 'test_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TestDetailView, self).get_context_data(**kwargs)
        context['questions'] = TestQuestion.objects.filter(test=self.object)
        return context


def create_test(request):
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        question_form = TestQuestionForm(request.POST)
        answer_form = TestAnswerForm(request.POST)

        if test_form.is_valid() and question_form.is_valid() and answer_form.is_valid():
            test = test_form.save()
            question = question_form.save(commit=False)
            answer = answer_form.save(commit=False)

            question.test = test
            question.save()

            answer.question = question
            answer.save()

            return redirect(reverse('test_detail', kwargs={'pk': test.id}))

    else:
        test_form = TestForm()
        question_form = TestQuestionForm()
        answer_form = TestAnswerForm()

    args = {}
    args.update(csrf(request))
    args['test_form'] = test_form
    args['question_form'] = question_form
    args['answer_form'] = answer_form

    return render(request, 'new_test.html', args)
