# 问题记录
## 新安装的mysql出现ERROR! The server quit without updating PID file
   很有可能是配置文件里的sock路径没有权限

## 在使用pymysql连接mysql时，需要制定字符集，否则会出现乱码
具体连接的参数如下：

param={
'host':'',
'port':...
'user':...
'password':...
'charset':'utf8',
'db':xxx
}

