from Common.eddid_sit_库链接 import SQL_Check

SQL_Check=SQL_Check()

def cd_clnt_apply_info(phone):
    print("查询申请单的手机号码为为：{}".format(phone))
    apply_id = SQL_Check.eddid_gfss_sit(database="eddid_gfss_sit",
                               sql="select apply_id from cd_clnt_apply_info where phone_no='{}'".format(
                                  phone))
    applyid=apply_id
    print("applyid值为:",applyid)
    return applyid
# print("apply_id为",apply_id)

# applyid=cd_clnt_apply_info(300642)
# print("applyid",applyid)