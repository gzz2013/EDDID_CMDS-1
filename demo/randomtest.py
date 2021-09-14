import random
#生成英文名字

EL=["Boyce","Elvis","Ziv","Eudolf","Steven","Tyrone","Owen","Herman","Andrew","Vic","Miles","Eonald","Wden","Will","Eock","Owen","Abbott","Cornelius","Dali","Fallon","Harsh","Kirby","Vvincent"]

EF=["Baker","Cook","Miller","Turner","Smith","London","Hall","Kent","Mill","Brook","Churchill","Hill","Green","Wood","Well","Brown","White","Longman","Sharp","Yonng","Back","Hand","Finger","Brain","Bird","Bull","Cotton","Fox","Stock","Cotton","Reed","George","Henry","David","Clinton","Macadam"]

Number="0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
FName=random.choice(EF)
LName=random.choice(EL)+random.choice(Number)

print("FName为：",FName)
print("LName为：",LName)

#生成中文名
CF=["李","王","张","刘","陈","杨","赵","冯","于","曹","袁","康","邱","秦","江","崔","白","郝","傅","曹","程","梁","胡","何","赵"]
CL=["彩绘","浪花","米猪","一手","蜜蜂","菜花","西瓜","油条","大佬","细佬","大山","哦耶","一龙","奶油","大锤","悠悠"]

ZFName=random.choice(CF)
XLName=random.choice(CL)+random.choice(Number)

print("ZFName为：",ZFName)
print("XLName为：",XLName)




#生成邮箱
# -*- coding:utf-8 -*-
def RandomEmail( emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com","@gzz.com","@edd.com"]
    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(9, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email

#生成随机金额
def randomAmount():
    a=float(random.randint(1,100))+float('%.2f'%(random.random()))
    return a





if __name__ == '__main__':
    print("生成随机金额:",randomAmount())
    print("随机邮箱:",RandomEmail())
    print(RandomEmail(emailType='@qq.com', rang=20))


