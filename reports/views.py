#coding=utf-8
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,get_object_or_404
from reports.models import *
from django.http import Http404
from django.core.urlresolvers import reverse

import pdb
import datetime,time,os,sys
from django.core.files import File
from generic import *

# Create your views here.
def index(request):
    latest_report_list = Report.objects.order_by('-create_time')[:10]
    context = {'latest_report_list': latest_report_list}
    return render(request, 'reports/index.html', context)

mrtg_image_dic={}
dnsla_image_dic={}
def create(request):
    """
    #为了保存image外键,建立report
    try:
        report=Report()
        report.save()
    except:
        pass
    

    mrtg_image_list=get_mrtg_image()
    """
    
    """
    mrtg_image_list=[]
    dnsla_image_list=[]
    return render(request, 'reports/create2.html', {
        "mrtg_image_list":mrtg_image_list,
        "mrtg_image_prefix":mrtg_image_prefix,
        "dnsla_image_list":dnsla_image_list,
        "dnsla_image_prefix":dnsla_image_prefix,
    })
    """
    # if this is a POST request we need to process the form data
    
    global mrtg_image_dic
    global dnsla_image_dic
    if request.method == 'POST':
        #从request的数据中,初始化一个表单
        form = ReportForm(request.POST)
        pdb.set_trace()
        #表单数据验证
        if form.is_valid():
            
            #验证成功,存入数据库
            ret=save_form(form)
            
            pdb.set_trace()
            view(request,ret['report_id'])
            return HttpResponseRedirect('/reports/')

    # if a GET (or any other method) we'll create a blank form
    else:
        #生成一个空的表单,非绑定
        form = ReportForm()
        #生成全局图像字典变量
        mrtg_image_dic=get_mrtg_image()
        dnsla_image_dic=dnsla_mrtg_image()
        
    
    
    return render(request, 'reports/create.html', {
            'form': form,
            'mrtg_image_dic':mrtg_image_dic,
            'mrtg_image_prefix':mrtg_image_prefix,
            'dnsla_image_dic':dnsla_image_dic,
            'dnsla_image_prefix':dnsla_image_prefix
            })
    
def save_form(form):
    pdb.set_trace()
    ret={'success':True,'error_message':'','report_id':0}
    try:
        start_time=form.cleaned_data['start_time']
        end_time=form.cleaned_data['end_time']

        report=Report(
            title=form.cleaned_data['title'],
            create_time=datetime.datetime.now(),
            persion=form.cleaned_data['persion'],
            abstract=form.cleaned_data['abstract'],
            process=form.cleaned_data['process'],
            start_time=start_time,
            end_time=end_time
        )
        report.save()
    except Exception,e:
        ret={'success':False,'error_message':str(e)}
        return ret
    #处理domain
    for domain in form.cleaned_data['domain'].split(':::'):
        if domain !='':
            try:
                dom=Domain.objects.get(domain_name=domain)
            except Domain.DoesNotExist:
                dom=Domain(domain_name=domain)
            try:
                #whois 查询
                import pythonwhois
                result=pythonwhois.get_whois(domain)
                dom.status=';'.join(result['status'])
                dom.registrant=result['contacts']['registrant']['name']
                dom.save()
                dom.report.add(report)
            except Exception,e:
                ret={'success':False,'error_message':str(e)}
                return ret

    for ip in form.cleaned_data['ip'].split(':::'):
        if ip !='':
            try:
                ip_obj=Ip.objects.get(addr=ip)
            except Ip.DoesNotExist:
                ip_obj=Ip(addr=ip)
                ip_obj.save()
                ip_obj.report.add(report)

    for i in form.cleaned_data['mrtg_image']:
        if mrtg_image_dic.has_key(str(i)):  
            try:
                img_name=mrtg_image_dic[str(i)]
                image=Mrtg_images(report=report,picture=img_name)
                image.save()
                
                try:
                    #start_time<end_time<end_time
                    pdb.set_trace()
                    node_qps=Qps.objects.filter(node_id=int(i),end_time__gt=start_time,end_time__lt=end_time)
                    for nq in node_qps:
                        inqps_list=[]
                        outqps_list=[]
                        inqps_list.append(nq.in_qps)
                        outqos_list.append(nq.out_qps)
                        #TODO nodes
                    max_qps=1
                    average_qps=1
                    att=Attact_node(report=report,nb=int(i))
                    
                except Exception,e:
                    pass
            except Exception,e:
                ret={'success':False,'error_message':str(e)}
                return ret
    for i in form.cleaned_data['dnsla_image']:
        if dnsla_image_dic.has_key(str(i)):  
            try:
                img_name=dnsla_image_dic[str(i)]
                image=Dnsla_images(report=report,picture=img_name)
                image.save()
            except Exception,e:
                ret={'success':False,'error_message':str(e)}
                return ret

    #TODO nodes
    ret['report_id']=report.id
    return ret

def new(request):
    pdb.set_trace()

def view(request,report_id):
    report = get_object_or_404(Report, pk=report_id)
    #pdb.set_trace()
    create_time=str(report.create_time.date())
    persions=report.persion.split(':::')
    
    year=report.start_time.year
    month=report.start_time.month
    day=report.start_time.day
    start_time=str(report.start_time.time())
    end_time=str(report.end_time.time())
    
    #nodes=report.nodes.all()
    attact_nodes=report.attact_nodes.all()
    for an in attact_nodes:
        try:
            node=Node.objects.get(nb=an.nb)
            an.name=node.name
            an.abbr=node.abbr
        except:
            continue
    
    processes=report.processes.all()
    for process in processes:
        process.time=str(process.create_time.time())
    
    mrtg_images=report.mrtg_images.all()
    
    dnsla_images=report.dnsla_images.all()
    
    
    context={
        'report':report,
        'create_time':create_time,
        'persions':persions,
        'year':year,'month':month,'day':day,
        'start_time':start_time,'end_time':end_time,
        'attact_nodes':attact_nodes,
        'processes':processes,
        'mrtg_images':mrtg_images,
        'dnsla_images':dnsla_images,
        
    }
    return render(request, 'reports/view.html', context)

def detail(request):
    pass

def get_mrtg_image():
    #格式化时间
    end_time=int(time.time())
    start_time=end_time-86400
	
    now=time.localtime(time.time())
    comment_now=time.strftime('%Y-%m-%d %H\:%M\:%S',now)
    file_time=time.strftime('%Y%m%d%H%M%S',now)
	
    
    rrd_files=os.popen("find "+ rrd_file_path +" -name *.rrd").read().strip().split('\n')

    mrtg_image_dic={}
    for rrd_file in rrd_files:
        
        image_file_name_key=rrd_file.replace(os.path.join(rrd_file_path,'cnqps_'),'').replace('.rrd','')
        try:
            #image_file_num=name_to_num[image_file_name_key]
            node=Node.objects.get(abbr=image_file_name_key)
            image_file_num=str(node.nb)
            node_name=node.name
        except:
            image_file_num='-1'
            node_name='空'
        image_file_name=image_file_name_key+'_'+image_file_num+'_'+file_time+'.png'
        image_file_path=os.path.join(mrtg_image_save_dir,image_file_name)
        #pdb.set_trace()
        os.popen('%s graph %s  --start %s --end %s         \
			     --title "Daily\' Graph (5 Minutes Average) "      \
			     --vertical-label "Bits Per second"               \
			     --height 400                      \
			     --width  1000                     \
			     --color "BACK#CCCCCC"             \
			     --color "CANVAS#CCFFFF"           \
			     --slope-mode                      \
			     --lower-limit 0                   \
			     DEF:value1=%s:ds0:AVERAGE   \
			     DEF:value2=%s:ds1:AVERAGE   \
			     DEF:value3=%s:ds0:MAX       \
			     DEF:value4=%s:ds1:MAX       \
			     COMMENT:"               Max              Average           Last\\n"  \
			     AREA:value1#00FF00:" In\\:"                \
			     GPRINT:value1:MAX:"%%10.2lf %%Sb/s"         \
			     GPRINT:value1:AVERAGE:"%%10.2lf %%sb/s"     \
			     GPRINT:value1:"LAST:%%10.2lf %%Sb/s"        \
			     COMMENT:" \\n"                             \
			     LINE3:value2#0000FF:"Out\\:"               \
			     GPRINT:value2:MAX:"%%10.2lf %%Sb/s"         \
			     GPRINT:value2:AVERAGE:"%%10.2lf %%Sb/s"     \
			     GPRINT:value2:LAST:"%%10.2lf %%Sb/S"        \
			     COMMENT:" \\n"                             \
			     COMMENT:"Last update\\: %s"'%(rrd_tool,image_file_path,start_time,end_time,rrd_file,rrd_file,rrd_file,rrd_file,str(comment_now)))
        
        mrtg_image_dic[image_file_num]=image_file_name
    return mrtg_image_dic

def dnsla_mrtg_image():
    pass


def sendmail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #pdb.set_trace()
            from django.core.mail import send_mail
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            #recipients = ['sunyuwu@cnnic.cn']
            #if cc_myself:
                #recipients.append(sender)

            #send_mail(subject, message, sender, recipients)
            
            import smtplib 
            smtp = smtplib.SMTP()   
            smtp.connect("smtp.126.com", "25")   
            smtp.login('sunyuwu0628', 'abc_25031874')   
            smtp.sendmail('sunyuwu0628@126.com', 'sunyuwu@cnnic.cn', 'From: sunyuwu0628@126.com/r/nTo: sunyuwu@cnnic.cn/r/nSubject: this is a email from python demo/r/n/r/nJust for test~_~')   
            smtp.quit()  
            return HttpResponseRedirect('/reports/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'reports/index.html', {'form': form})
    







