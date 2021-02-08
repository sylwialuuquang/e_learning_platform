from django.shortcuts import render
from django.views.generic import DetailView
from .models import Test, TestQuestion


class TestDetailView(DetailView):
    model = Test
    context_object_name = 'test'
    template_name = 'test_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TestDetailView, self).get_context_data(**kwargs)
        context['questions'] = TestQuestion.objects.filter(test=self.object)
        return context
