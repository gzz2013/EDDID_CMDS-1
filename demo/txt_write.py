from Config.cdms_config import *
from Common.data_文本读写 import *


L=[11,22,33,"ddd","sssadasds","wweqeqwewq",112222222]
de="22222"

# 将data写入文本
# data_write("F:\python\EDDID_CDMS\Data\userdatainf.txt",de)

a=data_read("/Data/userdatainf.txt")
print("读取文本的内容为%%%%%%%%%%%%%%%%%%%%%%%%%%%%", data_read("/Data/userdatainf.txt"))
print("读取文本的内容为%%%%%%%%%%%%%%%%%%%%%%%%%%%%", list(data_read("/Data/userdatainf.txt"))[0])
print("读取文本的内容为%%%%%%%%%%%%%%%%%%%%%%%%%%%%type：", type(data_read("/Data/userdatainf.txt")))
print("读取文本的内容为%%%%%%%%%%%%%%%%%%%%%%%%%%%%", type(list(data_read("/Data/userdatainf.txt"))))
print(list(data_read("/Data/userdatainf.txt")))

c=(a.strip('[')).strip(']')
print("c:",c)

b=c.replace("'","")
print("b::bb",b)
r=b.replace(" ","")
print("rrrrrr",r)

new3_list = r.split(",")

print("new3_listnew3_list:",new3_list,type(new3_list))