#coding:utf-8
from django.contrib import admin
from reports.models import *
# Register your models here.

class DnslaInline(admin.TabularInline):
    model= Dnsla_images
    extra = 3

class ProcessInline(admin.TabularInline):
    model=Process
    extra = 3

class AttactNodesInline(admin.TabularInline):
    model=Attact_node
    extra = 3


class ReportsAdmin(admin.ModelAdmin):
        fieldsets = [
            ('标题',     {'fields': ['title']}),
            ('摘要',     {'fields': ['abstract']}),
            ('创建时间', {'fields': ['create_time'], 'classes': ['collapse']}),
            ('值班人员', {'fields': ['persion']}),
            ('类型', {'fields': ['type']}),
            ('开始时间', {'fields': ['start_time']}),
            ('结束时间', {'fields': ['end_time']}),
            #('攻击域名', {'fields': [DomainInline]}),
            ('最大qps', {'fields': ['max_qps']}),
            #('攻击节点', {'fields': [NodesInline]}),
            #('攻击IP', {'fields': [IpInline]}),
            #('处理过程', {'fields': [ProcessInline]}),
            ('攻击是否已结束', {'fields': ['is_end']}),
            
        ]
        inlines = [DnslaInline,ProcessInline,AttactNodesInline]
        #要展示的列
        #list_display = ('question_text', 'pub_date', 'was_published_recently')
        #右侧的过滤器 ,按照发表时间过滤       
        #list_filter = ['pub_date']
        #上方增加搜索框
        #search_fields = ['question_text']

class DomainsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('报告',     {'fields': ['report']}),
        ('域名',     {'fields': ['domain_name']}),
        ('注册商',     {'fields': ['registrant']}),
        ('状态',     {'fields': ['status']}),
    ]

class IpsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('报告',     {'fields': ['report']}),
        ('ip',     {'fields': ['addr']}),
        ('origin',     {'fields': ['origin']}),
        ('类型',     {'fields': ['type']}),
    ]

class NodesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('nb',     {'fields': ['nb']}),
        ('abbr',     {'fields': ['abbr']}),
        ('name',     {'fields': ['name']}),
    ]

admin.site.register(Report,ReportsAdmin)
admin.site.register(Domain,DomainsAdmin)
admin.site.register(Ip,IpsAdmin)
admin.site.register(Node,NodesAdmin)

