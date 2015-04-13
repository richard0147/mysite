// 路径配置
require.config({
    paths: {
        echarts: 'js/dist'
    }
});
  // 使用
require(
    [
        'echarts',
        'echarts/chart/bar', // 使用柱状图就加载bar模块，按需加载
        'echarts/chart/line',
        'echarts/chart/pie'
    ],
    function (ec) {
        // 基于准备好的dom，初始化echarts图表
        var myChart = ec.init(document.getElementById('dnamechart')); 
        var chart1=ec.init(document.getElementById('addrchart'));
        var chart2=ec.init(document.getElementById('changedname'));
        var chart3=ec.init(document.getElementById('changeaddr'));
        var chart6=ec.init(document.getElementById('ports'));
        var option = {
            title:{
                text:'域名',
                x:'center'
            },
            tooltip: {
                trigger:'axis'

            },
            /*legend: {
                data:['域名']
            },*/
            xAxis : [
                {
                    type : 'value'
                }
            ],
            yAxis : [
                {
                    type : 'category',
                    data : ["molss.gov.cn.","tira.cn.","bta.net.cn.","people.com.cn.","3g.cn.","4.cn.","sinaimg.cn.",
                    "kuwo.cn.","zol-img.com.cn.","zhongchenggongyu.cn","lefeng.cn.","sina.com.cn.","online.sh.cn.",
                    "cdnetdns.cn.","in-addr.cn.","ce.cn.","cnnic.cn.","yihaodian.com.cn.","diditaxi.com.cn.","dns.com.cn",
                    "t.cn","mobage.com.cn.","ccgslb.com.cn.","dns.cn.","dynamic.163data.com.cn.","uc.cn.","cnradio.com.cn.",
                    "360.cn.","teny.cn.","IN-ADDR.ARPA."]
                }
            ],
            
            series : [
                {
                    "name":"",
                    "type":"bar",
                    "data":[10,10,10,10,10,10,10,10,11,11,11,11,11,11,12,12,12,12,13,13,13,13,13,13, 66, 51, 50, 46, 36,689]
                }
            ]
        };

        // 为echarts对象加载数据 
        myChart.setOption(option); 
        var option1 = {
            title : {
                text: 'IP地址',
                subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            tooltip: {
                trigger:'axis'

            },
            /*legend: {
                data:['域名']
            },*/
            xAxis : [
                {
                    type : 'value'
                }
            ],
            yAxis : [
                {
                    type : 'category',
                    data :["182.118.20.0","220.181.108.0","123.125.71.0","101.226.160.0","180.153.229.0","220.181.12.0","74.125.41.0",
                   "220.181.12.0","61.50.244.0"]
                }
            ],
            
            series : [
                {
                    "name":"",
                    "type":"bar",
                    "data":[10,10,12,36, 46, 50,51, 66,689]
                }
            ]
        };
        chart1.setOption(option1);       
    }
);
