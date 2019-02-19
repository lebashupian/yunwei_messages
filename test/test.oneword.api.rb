#!/opt/ruby_2.4.0/bin/ruby -w
# coding: utf-8
require 'net/http'
require 'uri'
require 'json'
#uri = URI('http://192.168.137.37:8888/msgs/json/?json={ "时间":"2018-10-12 10:10:01" , "来源":"192.168.1.100" ,"文件":"/var/log/messages","消息":"哈哈哈" ,"状态":"N" }')
loop {
Net::HTTP.post_form   URI('http://192.168.137.37:8888/oneword/postdata/'),
		{ "时间" => "2018-8-16" , "来源" => "mysql1921.68.1.100" , "内容" => "主机异常情况，异常码事发路口附近雷克萨解放拉萨324afal撒旦解放拉萨姐啊福克斯尽快立法建立健康了放松放松了福建省看来飞机昆仑山34","确认" => "N","关联用户" => "admin&wxl"}
sleep 0.5
}

##############################
# shell 命令 curl 方式提交，范例
# curl --connect-timeout 10 -d "时间=2018-10-12 10:10:01&来源=192.168.0.100&文件=/var/log/message&所有者=wxl&消息=aaa&状态=N" http://192.16:8888/msgs/postdata/
