#coding=utf-8
from django.core.management.base import BaseCommand
from reports.models import *

import os,pdb,sys,getopt
import time,datetime
from check_qps import *
from reports.models import *
from django.conf import settings

#rrdtool路径和rrd文件路径



#使用说明
def usage():
    print 'This script help get cnqps(sum/average) from rrdfile in any moment or perid of time.\n \
    options:\n\
    \t/usr/local/bin/python2.7 %s\n\
    \t-s,--start start time\n\
    \t-e,--end   end time\n\
    \t-t,--type  sum or average\n\
    \t-h,--help  print this help\n\
    \t--save     save data in sql \n\n\n \
    eg:\n\
    \t/usr/local/bin/python2.7 %s \\\n\
    \t--start="2014-10-28 12:00:00" \\\n\
    \t--end="2014-10-28 13:10:00" \\\n\
    \t--type="average"\\\n\
    \t--save'%(sys.argv[0],sys.argv[0])




def get_in_out_qps(start_time, end_time, start_time_second, end_time_second, save_sql):
    if start_time_second>end_time_second:
        usage()
        sys.exit()

    qps_dict={}
    rrd_tool=settings.RRD_TOOL
    #遍历每一个节点
    rrd_files=os.popen("find "+ settings.RRD_FILE_PATH +" -name *.rrd").read().strip().split('\n')
    for rrd_file in rrd_files:
        node_key=rrd_file.replace(os.path.join(settings.RRD_FILE_PATH,'cnqps_'),'').replace('.rrd','')
        print node_key+" start..."
        try:
            node=Node.objects.get(abbr=node_key)
            node_id=str(node.nb)
        except:
            node_id="-1"
            print "node is not exist in list, please update generic.py"
            continue
        #执行取数据命令
        qps_dict[node_id]={}
        #/opt/rrdtool-1.4.7/bin/rrdtool fetch /home/mrtg/mrtg/htdocs/cnqps/cnqps_sum.rrd AVERAGE --start 1414206299 --end 1414206299 -r 300
        command="%s fetch %s AVERAGE --start %s --end %s -r 300"%(rrd_tool,rrd_file,start_time_second,end_time_second)
        data_lines=os.popen(command).read().strip().split('\n')
        in_sum=0
        out_sum=0

        #处理数据
        for line in data_lines[2:]:
            time_strp=line.split(': ')[0]
            data_in=line.split(' ')[1]
            data_out=line.split(' ')[2]
            if (data_in.lower() in ["nan","-nan"]) or (data_out.lower() in ["nan","-nan"]):
                data_in='0'
                data_out='0'
            in_sum+=eval(data_in)
            out_sum+=eval(data_out)
            current_end_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(time_strp)))
            
            if save_sql==True:
                
                try:
                    Qps.objects.get(node_id=node_id,end_time=current_end_time)
                    print "\t%s %s data exist!"%(node_key,current_end_time)
                except Qps.DoesNotExist:
                    if (data_in.lower() in ["nan","-nan"]) or (data_out.lower() in ["nan","-nan"]):
                        data_in='0'
                        data_out='0'
                    in_qps=int(eval(data_in))
                    out_qps=int(eval(data_out))
                    check_flag=check_qps(int(time_strp),node_id,in_qps,out_qps)
                    qps=Qps(node_id=node_id,end_time=current_end_time,in_qps=in_qps,out_qps=out_qps,is_attact=check_flag)
                    qps.save()
                    print "\t%s %s data saved!"%(node_key,current_end_time)

        qps_dict[node_id]["in"]=in_sum*300
        qps_dict[node_id]["out"]=out_sum*300
        print node_key+" done.\n"
    return qps_dict

class Command(BaseCommand):
    def handle(self, *args, **options):
         #获取时间戳
         #参数
        opts,ages=getopt.getopt(sys.argv[1:],"hs:e:c:t:",["help","start=","end=","type=","save"])
        start_time_string=''
        end_time_string=''
        type=''
        save_sql=True
        for op,value in opts:
            if op=='-h' or  op=='--help':
                usage()
                sys.exit()
            elif op=='-s' or  op=='--start':
                start_time_string=value
            elif op=='-e' or  op=='--end':
                end_time_string=value
            elif op=='-t' or  op=='--type':
                type=value
            elif op=='--save':
                save_sql=True
            else:
                usage()
                sys.exit()
        if type=='':
            type="average"

        if start_time_string=='' or end_time_string=='':
            now=datetime.datetime.now()
            start=(now-datetime.timedelta(seconds=2470))
            start_time_string=start.strftime('%Y-%m-%d %H:%M:%S')
            #end_time_string=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            end=(now-datetime.timedelta(seconds=610))
            end_time_string=end.strftime('%Y-%m-%d %H:%M:%S')

        start_time=time.strptime(start_time_string,'%Y-%m-%d %H:%M:%S')
        end_time=time.strptime(end_time_string,'%Y-%m-%d %H:%M:%S')
        
        #获取时间戳秒数
        start_time_second=int(time.mktime(start_time))
        end_time_second=int(time.mktime(end_time))

        #获取qps进出总量
        qps_dict=get_in_out_qps(start_time_string, end_time_string, start_time_second, end_time_second,save_sql)

        #根据类型输出
        
        if len(qps_dict)!=0:
            in_sum=qps_dict['0']["in"]
            out_sum=qps_dict['0']["out"]
        else:
            return

        if type=='average':
            if end_time_second==start_time_second:
                print_in_time=int(in_sum)
                print_out_time=int(out_sum)
            else:
                print_in_time=int(in_sum/float(end_time_second-start_time_second))
                print_out_time=int(out_sum/float(end_time_second-start_time_second))
            print "in_qps=%s\tout_qps=%s"%(print_in_time,print_out_time)
        elif type=='sum':
            print "in_qps=%s\tout_qps=%s"%(int(in_sum),int(out_sum))
        else:
            print "unsupported type!"
            usage()        
























    

