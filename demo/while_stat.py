#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

#a=1继续等待；如果b=5继续循环；

def while_stat(a):
    c = 0
    while a <15:  # 该条件永远为true，循环将无限执行下去
        time.sleep(2)
        c += 1
        a+=1
        print("循环继续c:{},a:{}".format(c,a))
        if c==9:
            break

if __name__ == "__main__":

    while_stat(1)