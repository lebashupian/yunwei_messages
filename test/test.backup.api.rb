#!/opt/ruby_2.4.0/bin/ruby -w
# coding: utf-8
require 'net/http'
require 'uri'
require 'json'
#uri = URI('http://192.168.137.37:8888/msgs/json/?json={ "时间":"2018-10-12 10:10:01" , "来源":"192.168.1.100" ,"文件":"/var/log/messages","消息":"哈哈哈" ,"状态":"N" }')
loop {
Net::HTTP.post_form   URI('http://192.168.137.37:8888/backup/postdata/'),
		{ "备份日期" => "2018-9-28" , "备份时间" => "2018-9-28 10:10:10" , "备份来源" => "192.168.0.100","备份主机" => "webhost", "备份文件" => "/backup/1.txt" ,"备份状态" => "N","确认状态" => "N","备份项目" => "127.0.0.1-pgsql"}
sleep 0.5
}

##############################
# shell 命令 curl 方式提交，范例
# curl --connect-timeout 10 -d "时间=2018-10-12 10:10:01&来源=192.168.0.100&文件=/var/log/message&所有者=wxl&消息=aaa&状态=N" http://192.16:8888/msgs/postdata/
