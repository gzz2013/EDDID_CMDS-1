from Common.com_sql.eddid_sit_库链接 import SQL_Check

from Config.cdms_config import *

SQL_Check = SQL_Check()

sqldata=uatdatabase

# 通过phone查询applyid
def cd_clnt_apply_info(phone):
    print("查询申请单的手机号码为为：{}".format(phone))
    applyid = SQL_Check.eddid_gfss_sit(database=sqldata,
                               sql="select apply_id from cd_clnt_apply_info where phone_no='{}'".format(
                                  phone))
    # applyid=apply_id[0][0]
    # return applyid
    return applyid

#在cd_ac表查询符合条件的交易账号
def cd_ac(ac_stat, ac_catg, busin_acty_cde, clnt_id):
    # 通过phone查询applyid
    # print("查询申请单的手机号码为为：{}".format(clnt_id))
    ac_id = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select ac_id from cd_ac WHERE ac_stat='{}' AND ac_catg='{}' AND busin_acty_cde='{}' AND clnt_id='{}'".format(
                                         ac_stat, ac_catg, busin_acty_cde, clnt_id))
    accountId = ac_id[0][0]
    return accountId

#在通过交易证券账号和金额查询换汇申请单号
def cd_exch(clientId,applyAmount):
    exchorderinfor = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_exch WHERE clnt_id='{}' and apply_amt='{}'".format(clientId,applyAmount))

    return exchorderinfor

#通过phoen查询注册账户信息
def cd_enty(phone):
    userinformation = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="SELECT * FROM cd_enty WHERE phone='{}'".format(phone))
    return userinformation

def  cd_clnt_joint_enty(enty_id):
    cd_clnt_joint_enty = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_clnt_joint_enty where enty_id={}".format(enty_id))
    return cd_clnt_joint_enty


def  cd_ac(clnt_id):
    cd_ac = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_ac WHERE clnt_id={}".format(clnt_id))
    return cd_ac


def  cd_clnt(clnt_id):
    cd_clnt = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_clnt WHERE clnt_id={}".format(clnt_id))
    return cd_clnt

def  cd_ac_struc_appl(clnt_id):
    cd_ac_struc_appl = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_ac_struc_apply where clnt_id={} ".format(clnt_id))
    return cd_ac_struc_appl



if __name__=="__main__":
    # a=cd_ac('NORMAL','CASH','EQUITIES',11431)
    # print(a)
    print(cd_enty(16847802102))
    print("cd_enty:::",cd_enty(16847802102)[0][4])
    print("cd_clnt_apply_info:::",cd_clnt_apply_info(16847802102)[0][0])

    print("cd_enty2:::",cd_enty(16847802102)[0][0])
    print("cd_clnt_joint_enty:::",cd_clnt_joint_enty(cd_enty(16847802102)[0][0])[0][1])
    print("cd_ac:::", cd_ac(cd_clnt_joint_enty(cd_enty(16847802102)[0][0])[0][1])[0][0])
    print("cd_clnt:::", cd_clnt(500533)[0][3])
    print("cd_ac:::1111",cd_ac(11431))


