from django.urls import path

from . import views

# 二级路由
# 参数name url的名称 作用体现在html上 相当于在html文件可以通过 'app名称:url名称' 索引出某个url
app_name = 'polls'                                                          # 注意 这里必须注册一个命名空间
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),                        # /polls
    # DetailView 需要从URL获取主键值 
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),             # /polls/1
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),   # /polls/1/results
    path('<int:question_id>/vote/', views.vote, name = 'vote')                  # /polls/vote
]