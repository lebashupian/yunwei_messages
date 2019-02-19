#!/opt/ruby_2.2.3/bin/ruby -w
# coding: utf-8
require 'socket'
require 'pg'
begin
  server = TCPServer.open(9999)
  begin
    数据库对象 = PG::Connection.new(:host=>'127.0.0.1',:port=>'5432',:dbname=>'yunwei',:user=>'postgres_user',:password=>'')
  rescue
    puts "数据库不能连接"
  end
  loop {                       # 永久运行服务
    Thread.start(server.accept) do |link|
        str=link.gets  #读取link这个socket连接中的数据
        #p str
        shuzu=str.split(/-------/) #用--------来分割数据为数组对象
        时间=shuzu[0]  #获取认证名
        来源=shuzu[1]  #获取认证密码
        状态=shuzu[2]  #获取字符串数据
        消息=shuzu[3]  #获取字符串数据
        #"#{时间}","#{来源}","#{状态}","#{消息}
        sql=%Q{insert into msgs_消息 (时间,来源,消息,状态) values ("#{时间}","#{来源}","#{消息}","#{状态}")}
        #puts "#{sql}"
        数据库对象.query(sql);
        link.close      #关闭这个socket
    end
  }
rescue Interrupt
  puts "强制中断"
end 