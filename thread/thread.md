# Python 多进程

多进程包 multiprocessing

支持子进程、通信和共享数据，提供Process, Queue, Pipe, Lock

## Process
Process([group[,target[,name[,args[kwargs]]]]])

### 方法
is_alive, join(), run(), start(), terminate

### 属性：
authkey, daemon,exitcode,name, pid.daemon是父进程终止后自动终止，且自己不能产生新进程，必须在start
之前设置。
ddi
