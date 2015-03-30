from django.db import models

class Report(models.Model):
    title=models.CharField(max_length=50)
    create_time=models.DateTimeField(auto_now=True)
    #sunyuwu#=#liumingxing
    persion=models.CharField(max_length=100)
    abstract=models.CharField(max_length=1000)
    
    type=models.IntegerField(default=1)
    #last_time=models.TimeField()
    start_time=models.DateTimeField(auto_now=True)
    end_time=models.DateTimeField(auto_now=True)
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



    
    