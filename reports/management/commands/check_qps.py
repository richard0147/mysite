#coding=utf-8
from reports.models import *
import pdb
def get_qps(time_strp,node_id):
    in_qps=0
    out_qps=0
    i=0
    while in_qps==0 or out_qps==0:
        import time
        current_end_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_strp))
        try:
            qps=Qps.objects.filter(end_time=current_end_time,node_id=node_id)
            if len(qps=0):
                in_qps=0
                out_qps=0
                print "\t\tyesterday:%s no result"%(current_end_time)
            else:
                in_qps=qps[0].in_qps
                out_qps=qps[0].out_qps
                print "\t\tyesterday:%s in:%s out:%s"%(current_end_time,in_qps,out_qps)
        except:
            pass
        
        #important
        time_strp=time_strp-300
        i=i+1
        #获取临近5个点的qps
        if i>5:
            break
    return in_qps,out_qps

#检查qps是否遭受攻击
def check_qps(time_strp,node_id,in_qps,out_qps):
    time_strp_1=time_strp-86400
    time_strp_2=time_strp-86400*2

    #获取昨天和前天的qps in out值
    in_qps1,out_qps1=get_qps(time_strp_1,node_id)
    in_qps2,out_qps2=get_qps(time_strp_2,node_id)
    
    if in_qps1<in_qps2:
        standard_in=in_qps1
    else:
        standard_in=in_qps2
    
    if out_qps1<out_qps2:
        standard_out=out_qps1
    else:
        standard_out=out_qps2

    if in_qps1==0 or out_qps1==0 or in_qps2==0 or out_qps2==0:
        return 0
    elif in_qps > 2*standard_in or out_qps > 2*standard_out:
        print "\t\t attack!"
        return 1
    else:
        return 0
