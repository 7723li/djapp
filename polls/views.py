from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

# ListView 显示一个对象的列表
class IndexView(generic.ListView):
    template_name = "polls_template/index.html"
    context_object_name  = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

# DetailView 显示特定类型对象的详细页面 根据主键进行数据库取值
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls_template/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls_template/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        # 从post方法获取'choice'字段的内容 类似json 具体看html
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "no choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # 重定向到投票结果界面
        return HttpResponseRedirect(reverse('polls:results', args = (question.id, )))