from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Choice

# 内联模型
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 加入字段分界描述
    fieldsets = [
        (None,                  {'fields' : ['question_text']}),
        ('Date information',    {'fields' : ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # 增加一个基于pub_date的过滤面板
    search_fields = ['question_text'] # 增加一个基于问题描述的搜索栏

admin.site.register(Question, QuestionAdmin)   # 注册应用
#admin.site.register(Choice)