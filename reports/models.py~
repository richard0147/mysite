#coding=utf-8
from django.db import models

class Report(models.Model):
    title=models.CharField(max_length=50)
    create_time=models.DateTimeField()
    #sunyuwu#=#liumingxing
    persion=models.CharField(max_length=100)
    abstract=models.CharField(max_length=2000)
    
    process=models.CharField(max_length=2000)
    type=models.IntegerField(default=1)
    #last_time=models.TimeField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    max_qps=models.IntegerField(default=0)
    is_end=models.BooleanField(default=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Process(models.Model):
    report=models.ForeignKey(Report,related_name='processes')
    create_time=models.DateTimeField()
    content=models.CharField(max_length=200)

class Attact_node(models.Model):
    report=models.ForeignKey(Report,related_name='attact_nodes')
    nb=models.IntegerField()
    max_qps=models.IntegerField()
    average_qps=models.IntegerField()
    picture=models.ImageField(upload_to='mrtg')
    dnsla_json=models.CharField(max_length=2000)

class Domain(models.Model):
    report=models.ManyToManyField(Report,related_name='domains')
    domain_name=models.CharField(max_length=100,unique=True)
    registrant=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.domain_name
class Ip(models.Model):
    report=models.ManyToManyField(Report,related_name='ips')
    addr=models.GenericIPAddressField(unique=True)
    origin=models.CharField(max_length=50,default='')
    # 0 means client , 1 means recursion
    type=models.IntegerField(default=0)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.addr
class Qps_snapshots(models.Model):
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    create_time=models.DateField(auto_now_add=True)

class Qps(models.Model):
    snap_id=models.ForeignKey(Qps_snapshots)
    node_id=models.IntegerField(default=0)
    end_time=models.DateTimeField()
    in_qps=models.IntegerField(default=0)
    out_qps=models.IntegerField(default=0)
    is_attact=models.IntegerField(default=0)

class Node(models.Model):
    nb=models.IntegerField(unique=True)
    abbr=models.CharField(max_length=50)
    name=models.CharField(max_length=50)


from django import forms
from django.forms import widgets

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cc_myself =forms.BooleanField(required=False)



class processWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        _widgets = (
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
        )
        super(processWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(':::')[0:5]
        return ['', '', '', '', '']

class ProcessMultiField(forms.MultiValueField):
    widget = processWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=400),
            forms.CharField(max_length=300),
        )
        super(ProcessMultiField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return ':::'.join(data_list)
        return ''

class PersionWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        _widgets = (
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
        )
        super(PersionWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(':::')[0:5]
        return ['', '', '', '', '']

class PersionMultiField(forms.MultiValueField):
    widget = PersionWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
        )
        super(PersionMultiField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return ':::'.join(data_list)
        return ''


mrtgChoices=(('0', u'SUM'), ('1', u'主节点'), ('2', u'瑞典'), ('4', u'成都电信'), ('5', u'广州移动'), ('6', u'韩国'), ('7', u'德国'), ('8', u'美国Neustar'), ('9', u'香港'), ('10', u'美国ISC'), ('11', u'广州电信'), ('12', u'英国'), ('13', u'西安电信'), ('14', u'南京联通'), ('15', u'广州联通'), ('16', u'南京电信'), ('17', u'济南联通'), ('18', u'沈阳联通'), ('19', u'北京移动'), ('20', u'上海电信'), ('21', u'杭州阿里'), ('24', u'长城网'), ('25', u'曼彻斯特'), ('26', u'新加坡'), ('27', u'芝加哥'), ('29', u'荷兰'), ('30', u'北京联通'), ('31', u'美国达拉斯'))
#mrtgChoices

class ReportForm(forms.Form):

    title=forms.CharField(
        max_length=50,
        label='标题',
        initial='CNQPS故障报告',
        help_text='',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    start_time=forms.DateTimeField(
        label='开始时间',
        widget=forms.DateTimeInput(attrs={'class': 'form-control ui_timepicker','placeholder':'请输入开始时间'})
    )
    
    end_time=forms.DateTimeField(
        label='结束时间',
        widget=forms.DateTimeInput(attrs={'class': 'form-control ui_timepicker','placeholder':'请输入结束时间'})
    )
    
    persion=PersionMultiField(
        required=False,
        label='参与人员',
        widget=PersionWidget(attrs={'class': 'form-control persion-format','placeholder':'请输入参与人员'})
    )
    
    domain=PersionMultiField(
        required=False,
        label='攻击域名',
        widget=PersionWidget(attrs={'class': 'form-control domain-format','placeholder':'请输入攻击域名'})
    )
    
    ip=PersionMultiField(
        required=False,
        label='来源IP',
        widget=PersionWidget(attrs={'class':'form-control ip-format','placeholder':'请输入来源IP'})
    )
    
    abstract=forms.CharField(
        max_length=2000,
        label='故障摘要',
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'请输入故障摘要'})
    )
    
    process=ProcessMultiField(
        required=False,
        label='处理过程',
        widget=processWidget(attrs={'class': 'form-control process-format','placeholder':'请输入处理过程'})
    )
    
    mrtg_image=forms.TypedMultipleChoiceField(
        required=False,
        choices=mrtgChoices,
        label='MRTG图像',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'mrtg-format'})
    )



