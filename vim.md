1 set tabstop=4
2 set shiftwidth=4
3 set expandtab
4 set fileformat=unix
5 set nobomb
6 set ff=unix
7 set fileencodings=utf-8.ucs-born.cp936
8 syntax on
9 set nocompatible
10 set completeopt=preview
11 set ai
12 
13 set nu



## 分屏：

分屏启动Vim
使用大写的O参数来垂直分屏。
vim -On file1 file2 ...
使用小写的o参数来水平分屏。
vim -on file1 file2 ...
注释: n是数字，表示分成几个屏。

关闭分屏
关闭当前窗口。
Ctrl+W c
关闭当前窗口，如果只剩最后一个了，则退出Vim。
Ctrl+W q
分屏
上下分割当前打开的文件。
Ctrl+W s
上下分割，并打开一个新的文件。
:sp filename
左右分割当前打开的文件。
Ctrl+W v
左右分割，并打开一个新的文件。
:vsp filename
移动光标
Vi中的光标键是h, j, k, l，要在各个屏间切换，只需要先按一下Ctrl+W

把光标移到右边的屏。
Ctrl+W l
把光标移到左边的屏中。
Ctrl+W h
把光标移到上边的屏中。
Ctrl+W k
把光标移到下边的屏中。
Ctrl+W j
把光标移到下一个的屏中。.
Ctrl+W w
移动分屏
这个功能还是使用了Vim的光标键，只不过都是大写。当然了，如果你的分屏很乱很复杂的话，这个功能可能会出现一些非常奇怪的症状。

向右移动。
Ctrl+W L
向左移动
Ctrl+W H
向上移动
Ctrl+W K
向下移动
Ctrl+W J
屏幕尺寸
下面是改变尺寸的一些操作，主要是高度，对于宽度你可以使用[Ctrl+W <]或是[Ctrl+W >]，但这可能需要最新的版本才支持。

让所有的屏都有一样的高度。
Ctrl+W =
增加高度。
Ctrl+W +
减少高度。
Ctrl+W -
