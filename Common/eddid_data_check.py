from Common.eddid_sit_库链接 import SQL_Check

SQL_Check=SQL_Check()

def cd_clnt_apply_info(phone):
    apply_id = SQL_Check.eddid_gfss_sit(database="eddid_gfss_sit",
                               sql="select apply_id from cd_clnt_apply_info where phone_no='{}';".format(
                                  phone))
    return apply_id
# print("apply_id为",apply_id)

# apply_id=cd_clnt_apply_info()
# print("apply_id为",apply_id)