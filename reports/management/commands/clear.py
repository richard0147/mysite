#coding=utf-8
#django command import
from django.core.management.base import BaseCommand
from reports.models import *
import os
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        nodes=Node.objects.all()
        for node in nodes:
            print "delete node:%s"%(node.name)
            node.delete()

        objs=Ip.objects.all()
        for obj in objs:
            print "delete Ip:%s"%(obj.addr)
            obj.delete()
        
        objs=Domain.objects.all()
        for obj in objs:
            print "delete Domain:%s"%(obj.domain_name)
            obj.delete()
        
        objs=Attact_node.objects.all()
        for obj in objs:
            try:
                picture_path=os.path.join(settings.MEDIA_ROOT,obj.picture.url[1:])
                if os.path.isfile(picture_path):
                    os.remove(picture_path)
                    print "delete picture:%s"%(picture_path)
            except:
                pass
            finally:
                print "delete Attact_node:%s"%(obj.nb)
                obj.delete()
        
        objs=Report.objects.all()
        for obj in objs:
            print "delete Report:%s"%(obj.title)
            obj.delete()
        
        picture_path=os.path.join(settings.MEDIA_ROOT,settings.MEDIA_URL[1:])
        if os.path.isfile(picture_path):
            print "delete useless picture:%s"%(obj.picture_path)
            os.remove(picture_path)
