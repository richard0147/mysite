#coding=utf-8
#django command import
from django.core.management.base import BaseCommand
from reports.models import *
import datetime,time
import pdb

class Command(BaseCommand):
    def handle(self, *args, **options):
        init_nodes()
        init_reports()

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def init_reports():
    fcn=open('/home/richard/develop/mysite/reports/management/commands/CN_Attack_History.json','r')
    import json
    cn_report_list=json.loads(fcn.readline())
    try:
        for cn_report in cn_report_list:
            print "start..."
            report_id=cn_report["id"]
            create_time=datetime.datetime.strptime(cn_report["Date"], "%Y-%m-%d")
            if cn_report["StartTime"]==None:
                start_time=create_time
            else:
                try:
                    start_time=datetime.datetime.strptime(cn_report["StartTime"], "%Y-%m-%d")
                except:
                    start_time=datetime.datetime.strptime(cn_report["StartTime"], "%Y-%m-%d %H:%M:%S")
            
            if cn_report["StopTime"]==None:
                end_time=create_time+datetime.timedelta(days=1)
            else:
                try:
                    end_time=datetime.datetime.strptime(cn_report["StopTime"], "%Y-%m-%d")
                except:
                    end_time=datetime.datetime.strptime(cn_report["StopTime"], "%Y-%m-%d %H:%M:%S")
            
            domain_list=cn_report["DomainName"].split(',')
            ip_list=cn_report["IP_Information"].split(',')
            
            if cn_report["RegisterName"]==None:
                reigistrant=u"暂无"
            else:
                reigistrant=cn_report["RegisterName"]
                
            if cn_report['PeekFlow']==None:
                max_qps=0
            else:
                max_qps=cn_report['PeekFlow']
            abstract=u"自%s至%s,cn顶级节点遭受攻击,攻击域名为以%s结尾的%s,所属注册商为:%s,IP信息:%s,受影响的节点:%s. 攻击持续时间%s小时.QPS峰值为%s次每秒"%(str(create_time),str(end_time),cn_report["DomainName"],str(cn_report["Remark"]),reigistrant,cn_report["IP_Information"],str(cn_report["Sites_Impact"]),str(cn_report["Duration"]),str(cn_report["PeekFlow"]))
            report=Report(title="CNQPS故障报告",create_time=create_time,start_time=start_time,end_time=end_time,max_qps=int(max_qps),process="",persion="",abstract=abstract)
            report.save()
            print "save report:%s"%(report.title)
            for domain_name in domain_list:
                try:
                    domain=Domain.objects.get(domain_name=domain_name)
                    domain.report.add(report)
                    print "\treleted doamin:%s"%(domain_name)
                except Domain.DoesNotExist:
                    domain=Domain(domain_name=domain_name)
                    domain.status=''
                    domain.registrant=''
                    domain.save()
                    domain.report.add(report)
                    print "\tsave doamin:%s"%(domain_name)
            for ip in ip_list:
                if ip==None or ip=="":
                    print "\tpass ip:%s"%(ip)
                    continue
                try:
                    ip_obj=Ip.objects.get(addr=ip)
                    ip_obj.report.add(report)
                    print "\treleted ip:%s"%(ip)
                except Ip.DoesNotExist:
                    ip_obj=Ip(addr=ip)
                    ip_obj.save()
                    ip_obj.report.add(report)
                    print "\tsave ip:%s"%(ip)
            print "end..."
    except Exception,e:
        print e
    fcn.close()
    

def init_nodes():
    #nodes
    node=Node(nb=0,abbr='sum',name='SUM')
    node.save()
    node=Node(nb=1,abbr='bjcst',name='主节点')
    node.save()
    node=Node(nb=2,abbr='senetnod',name='瑞典')
    node.save()
    node=Node(nb=4,abbr='cdtel',name='成都电信')
    node.save()
    node=Node(nb=5,abbr='gzmob',name='广州移动')
    node.save()
    node=Node(nb=6,abbr='krkisa',name='韩国')
    node.save()
    node=Node(nb=7,abbr='denic',name='德国')
    node.save()
    node=Node(nb=8,abbr='usneus',name='美国Neustar')
    node.save()
    node=Node(nb=9,abbr='hkcuhk',name='香港')
    node.save()
    node=Node(nb=10,abbr='usisc',name='美国ISC')
    node.save()
    node=Node(nb=11,abbr='gztel',name='广州电信')
    node.save()
    node=Node(nb=12,abbr='uktata',name='英国')
    node.save()
    node=Node(nb=13,abbr='xatel',name='西安电信')
    node.save()
    node=Node(nb=14,abbr='njuni',name='南京联通')
    node.save()
    node=Node(nb=15,abbr='gzuni',name='广州联通')
    node.save()
    node=Node(nb=16,abbr='njtel',name='南京电信')
    node.save()
    node=Node(nb=17,abbr='jnuni',name='济南联通')
    node.save()
    node=Node(nb=18,abbr='syuni',name='沈阳联通')
    node.save()
    node=Node(nb=19,abbr='bjmob',name='北京移动')
    node.save()
    node=Node(nb=20,abbr='shtel',name='上海电信')
    node.save()
    node=Node(nb=21,abbr='hzal',name='杭州阿里')
    node.save()
    node=Node(nb=24,abbr='bjcgw',name='长城网')
    node.save()
    node=Node(nb=25,abbr='ukman',name='曼彻斯特')
    node.save()
    node=Node(nb=26,abbr='sgtata',name='新加坡')
    node.save()
    node=Node(nb=27,abbr='useqix',name='芝加哥')
    node.save()
    node=Node(nb=29,abbr='nlotdeasynet',name='荷兰')
    node.save()
    node=Node(nb=30,abbr='bjbtc',name='北京联通')
    node.save()
    node=Node(nb=31,abbr='usncc',name='美国达拉斯')
    node.save()
    
