#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time


#a=1继续等待；如果b=5继续循环；

def while_stat(stat,vear):
    c = 0
    while stat!=vear:  # 该条件永远为true，循环将无限执行下去
        time.sleep(2)
        c += 1
        stat+=1
        print("var为a循环继续",format(c))

if __name__ == "__main__":
    stat="dcc"
    vear="dcc"
    while_stat("dcc","dcc")