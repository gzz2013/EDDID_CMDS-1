from Common.com_sql.eddid_sit_库链接 import SQL_Check
from Config.cdms_config import *

SQL_Check = SQL_Check()

sqldata=uatdatabase
# sqldata=sitdatabase

def cd_clnt_wc_match(phone):
    #cd_clnt_wc_match 修改world check的审核状态都为通过
    SQL_Check.eddid_gfss_sit(database=sqldata,
                             sql="update cd_clnt_wc_match set resolution_status='FALSE'  where wc_case_id IN(select id from cd_clnt_wc_case where check_id in(select id from  cd_clnt_check_info where apply_id in (select apply_id from cd_clnt_apply_basisinfo where apply_no in (SELECT apply_no applyno FROM cd_clnt_apply_basisinfo WHERE apply_id =(select apply_id from cd_clnt_apply_info where phone_no='{}' ORDER BY init_time DESC LIMIT 1)))))".format(
                                 phone))

# print("apply_id为",apply_id)

# apply_id=cd_clnt_apply_info()
# print("apply_id为",apply_id)
