from django.urls import path

from . import views

# 二级路由
# 参数name url的名称 作用体现在html上 相当于在html文件可以通过 'app名称:url名称' 索引出某个url
app_name = 'polls'                                                          # 注意 这里必须注册一个命名空间
urlpatterns = [
    path('', views.index, name = 'index'),                                  # /polls
    path('<int:question_id>/', views.detail, name = 'detail'),             # /polls/1
    path('<int:question_id>/results', views.results, name = 'results'),    # /polls/1/results
    path('<int:question_id>/vote', views.vote, name = 'vote')              # /polls/vote
]