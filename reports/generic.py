#coding=utf-8
#rrd_tool="/opt/rrdtool-1.4.7/bin/rrdtool"
#rrd_file_path="/home/mrtg/mrtg/htdocs/cnqps/"
rrd_tool="/usr/bin/rrdtool"
rrd_file_path="/home/richard/develop/mysite/mrtg"
mrtg_image_save_dir="/home/richard/develop/mysite/media/mrtg/"
dnsla_dname_url="http://218.241.118.153:8090/Index/Show/getDnameRankById/nodeid/%s"
dnsla_addr_url="http://218.241.118.153:8090/Index/Show/getAddrRankById/nodeid/%s"

#全局字典变量
name_to_num={
	'jnuni':'17',
	'nlotdeasynet':'29',
	'gzuni':'15',
	'gztel':'11',
	'bjcst':'1',
	'usisc':'10',
	'bjcgw':'24',
	'krkisa':'6',
	'sum':'0',
	'syuni':'18',
	'shctt':'22',
	'denic':'7',
	'bjciet':'25',
	'njtel':'16',
	'xatel':'13',
	'uktata':'12',
	'shtel':'20',
	'cdtel':'4',
	'usncc':'31',
	'usneus':'8',
	'njuni':'14',
	'gzmob':'5',
	'bjcer':'23',
	'bjbtc':'30',
	'bjmob':'19',
	'senetnod':'2',
	'useqix':'27',
	'hkcuhk':'9',
	'sgtata':'26'
}
