#coding:utf-8
from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline]
        #要展示的列
        list_display = ('question_text', 'pub_date', 'was_published_recently')
        #右侧的过滤器 ,按照发表时间过滤       
        list_filter = ['pub_date']
        #上方增加搜索框
        search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)
