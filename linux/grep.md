# grep命令
在每个文件或者标准输出中查找制定的模式
## 语法
   grep [选项] ... PATTERN [FILE]

   默认情况下，使用的是基本正则表达式(BRE)
   
   eg:
   
   grep -i 'hello world' menu.h main.c

## 选项：
###  正则选择和解释
  -E, --extended-regexp 使用扩展表达式
  
  -F, --fixed-strings 模式是新行分割的固定字符串集合
  
  -G, --basic-regexp
  
  -P, --perl-regexp
  
  -e ,--regexp==PATTERN, 使用模式搜索
  
  -f, --file=FILE，从文件中获取模式
  
  -i, --ignore-case,忽略大小写
  
  -w, --word-regexp 强制模式匹配整个字
  
  -x, --line-regexp 整个行
### 工具选项
 -s, --no-messages 抑制错误
 
 -v， --invert-match 选择不匹配的行，
 
 -V, --vesion 显示版本信息

### 输出控制
 -m, --max-count=NUM， NUM次匹配后退出
 
 -b, --byte-offset，打印字节偏移
 
 -n， --line-number，行号
 
 -H，--with-filename 文件名
 
 -h
