# 1.this project is neceserry to work at venv(virturlenv)/mysite/</br>

# 2.MySQL
2.1 must run "CREATE DATABASE sb;" in *mysql command line* before run the server</br>
2.2
* 在models.py中修改模型
* 运行python manage.py makemigrations为改动创建迁移记录
* 运行python manage.py sqlmigrate polls 0001 展示SQL语句
* 运行python manage.py check 检查项目中的错误
* 运行python manage.py migrate，将操作同步到数据库

[Part 1：请求与响应](http://www.liujiangblog.com/course/django/87)
[Part 2：模型与后台](http://www.liujiangblog.com/course/django/88)