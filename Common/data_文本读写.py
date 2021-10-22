#-*- coding:utf-8 -*-

def data_read(file):
    with open(file, 'r',encoding="utf-8") as data_txt:
        for text in data_txt.readlines():
            return text

def data_write(file,d):
    with open(file,'w',encoding="utf-8") as data_txt:
        # data_txt.write(str(d))
        data_txt.writelines(str(d))
        # data_txt.writelines("d,",{str(d)})

# 将从txt的列表数据中提取后转为LIST
def datahandle(data):
    #['10949311037', 'G74lhvoI@189.com', 'Hillv', 'Harsh', '冯细佬S', '110101199808231142']原始字符串
    # 去掉“[”和“]”
    c = (data.strip('[')).strip(']')
    # 去掉“‘”单引号
    b = c.replace("'", "")
    #去掉“ ”空格
    r = b.replace(" ", "")
    # 将字符串以“,”进行分段生成列表
    enddate = r.split(",")
    return enddate


if __name__=='__main__':
    # data_write(file="F:\python\EDDID_CDMS\Data\userdatainf.txt", d='222')
    q=data_read("/Data/userdatainf.txt")
    print("datahandle(q)",datahandle(q),type(datahandle(q)))