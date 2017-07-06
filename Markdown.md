Markdown语法学习
============

Markdown learn
---

# H1
...

###### H6

*这时 斜体*
_ysy

_这时测试_

**这时粗体**
__这时粗体__

+ 这时无序列表
+ 这时无序列表

* 这时无序列表
* 这时无序列表

- 这时无序列表
- 这时无序列表

1. this is order table
2. This is order


### 链接
This is an [example links](https://www.google.com)


I get 10 times more traffic from [Google][1] than from [Yahoo][2] or [MSN][3].  

[1]: http://google.com/        "Google" 
[2]: http://search.yahoo.com/  "Yahoo Search" 
[3]: http://search.msn.com/    "MSN Search"


. 图片（Images）
图片的处理方式和链接的处理方式，非常的类似。
内联方式：![alt text](/path/to/img.jpg "Title")
引用方式：
![alt text][id] 

[id]: /path/to/img.jpg "Title"

9. 代码（HTML中所谓的Code）
实现方式有两种：
第一种：简单文字出现一个代码框。使用`<blockquote>`。（`不是单引号而是左上角的ESC下面~中的`）
第二种：大片文字需要实现代码框。使用Tab和四个空格。

10. 脚注（footnote）
实现方式如下：
hello[^hello]


[^hello]: hi

11. 下划线
在空白行下方添加三条“-”横线。（前面讲过在文字下方添加“-”，实现的2级标题）


`import test`
