from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 发布时间 >= 当前时间 - 当前的一天之前 (具体到毫秒)
        now = timezone.now()
        # 最迟发布时间 不应该超过现在
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now

    # 管理界面 添加可以根据"是否最近发布"进行排序的属性
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently'

    question_text = models.CharField(max_length = 256)  # 问题描述
    pub_date = models.DateTimeField('date published')   # 问题时间

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    # 注意要将外键写在'多'的一方 每一个Choice关联到一个对应的Question
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 256)    # 选项描述
    votes = models.IntegerField(default = 0)            # 已选选项