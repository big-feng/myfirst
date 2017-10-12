#!/usr/bin/python
#coding=utf-8
import time
a=0
f=file('/home/bigfeng/ceshi.txt','a')   #日志文件路径
while 1:
    t=time.time()
    if a==10:             #计时器a达到10s关闭文件并退出循环 
        f.close()
        break
    elif t%1==0:     #整数时间，即每过一秒，计时器加 1
        a=a+1
        for i in range(10000):  
            f.write("hello\n")  #需要写入日志内容的代码
