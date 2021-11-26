import hashlib
def MD5_Encrypt(str):
    # 创建md5对象
    m = hashlib.md5()
    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    str_MD5=str_md5.upper()
    # print('MD5加密前为 ：' + str)
    print('MD5加密后为 ：' + str_MD5)
    # str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
    # # print('MD5加密后为 ：' + str_md5)
    return str_MD5

# if __name__=="__main__":
#     # a=AES_Encrypt(data="91110105MA01QLYL5A")
#     # print(a)
#     b=MD5_Encrypt(str="111111")
#     print(b)