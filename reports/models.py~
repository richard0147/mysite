#coding=utf-8
from django.db import models

class Report(models.Model):
    title=models.CharField(max_length=50)
    create_time=models.DateTimeField()
    #sunyuwu#=#liumingxing
    persion=models.CharField(max_length=100)
    abstract=models.CharField(max_length=1000)
    
    type=models.IntegerField(default=1)
    #last_time=models.TimeField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    max_qps=models.IntegerField(default=0)
    is_end=models.BooleanField(default=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title


class Mrtg_images(models.Model):
    report=models.ForeignKey(Report,related_name='mrtg_images')
    picture=models.ImageField(upload_to='mrtg')

class Dnsla_images(models.Model):
    report=models.ForeignKey(Report,related_name='dnsla_images')
    picture=models.ImageField(upload_to='dnsla')

class Process(models.Model):
    report=models.ForeignKey(Report,related_name='processes')
    create_time=models.DateTimeField()
    content=models.CharField(max_length=200)

class Attact_node(models.Model):
    report=models.ForeignKey(Report,related_name='attact_nodes')
    nb=models.IntegerField()
    max_qps=models.IntegerField()
    average_qps=models.IntegerField()

class Domain(models.Model):
    report=models.ManyToManyField(Report,related_name='domains')
    domain_name=models.CharField(max_length=100)
    registrant=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.domain_name
class Ip(models.Model):
    report=models.ManyToManyField(Report,related_name='ips')
    addr=models.IPAddressField()
    origin=models.CharField(max_length=50)
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
    nb=models.IntegerField()
    abbr=models.CharField(max_length=50)
    name=models.CharField(max_length=50)


from django import forms
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)



from django.forms import widgets
class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        _widgets = (
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(':::')[0:5]
        return [None, None, None]

class TestMultiField(forms.MultiValueField):
    widget = DateSelectorWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
        )
        super(TestMultiField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return ':::'.join(data_list)
        return ''

class ReportForm(forms.Form):
    title=forms.CharField(max_length=50,label='标题',initial='CNQPS故障报告',help_text='50 characters max.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    start_time=forms.DateTimeField(label='开始时间')
    end_time=forms.DateTimeField(label='结束时间')
    persion=forms.CharField(max_length=100,label=('参与人员','asdfasdf'))
    domain=forms.MultipleChoiceField(label='攻击域名')
    ip=forms.MultiValueField(label='来源IP',widget=forms.TextInput(attrs={'class': 'form-control'}))
    abstract=forms.CharField(max_length=100,label='故障摘要',widget=forms.Textarea)
    process=TestMultiField()
    mrtg_image=forms.TypedMultipleChoiceField(
        required=False,
        choices=(('leve1', '差评'),('leve2', '中评'),('leve3', '1好评')),
        label='MRTG图像',
        widget=forms.CheckboxSelectMultiple
    )
    dnsla_image=forms.MultipleChoiceField(label='DNSLA图像')



