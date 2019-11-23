# 1.this project is neceserry to work at venv(virturlenv)/mysite/

# 2.MySQL
2.1 must run "CREATE DATABASE ***sb(super base)***;" in *mysql command line* before run the server
2.2
* 在models.py中修改模型
* 运行python manage.py makemigrations为改动创建迁移记录
* 运行python manage.py sqlmigrate polls 0001 展示SQL语句
* 运行python manage.py check 检查项目中的错误
* 运行python manage.py migrate，将操作同步到数据库
2.3
* models.Model.get 精准取值(1个)
* models.Model.filter 模糊取值(多个)

# 3.templates
* 浏览器中访问/polls/34/: 
    1. *ROOT_URLCONF = 'mysite.urls'* in *setting.py*
    2. 加载*mysite*.urls模块
    3. ->二级路由->三级路由..逐级匹配urlpatterns
*   查找模板文件
    1. *'BACKEND': 'django.template.backends.django.DjangoTemplates'* in *setting.py*
    2. 'APP_DIRS': ***True*** *在每个 INSTALLED_APPS 文件夹中寻找 "templates" 子目录*
    3. Django 会寻找到对应的app_directories 
        例：本项目 只需要使用*polls/index.html*就可以引用到*polls/templates/polls/index.html*
        *实际上没有这么干 不然名称太乱*

# 4.static
* settings.py -> STATIC_URL = '/static/' -> 资源

[Part 1：请求与响应](http://www.liujiangblog.com/course/django/87)
[Part 2：模型与后台](http://www.liujiangblog.com/course/django/88)
[Part 3：视图和模板](http://www.liujiangblog.com/course/django/89)
[Part 4：表单和类视图](http://www.liujiangblog.com/course/django/90)
[Part 5：测试](http://www.liujiangblog.com/course/django/91)
[Part 6：静态文件](http://www.liujiangblog.com/course/django/92)