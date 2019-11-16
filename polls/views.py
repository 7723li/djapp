from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import Question

# Create your views here.

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]      # 根据pub_date排序
    context = {
        "latest_question_list" : lastest_question_list
    }

    return render(request, 'polls_template/index.html', context)    # 请求对象 模板 传递给模板的数据

    '''
    or =>
    template = loader.get_template("polls_template/index.html")
    return HttpResponse(template.render(context, request))
    '''

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)    # 后面可以跟上任意个数的关键字参数 使用的是filter方法
    '''
    or =>
    try:
        question = Question.objects.get(pk = question_id)
    except:
        raise Http404("question does not exist")
    '''

    return render(request, "polls_template/details.html", {'question' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)