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


#通过交易证券账号和金额查询出金申请单号
def  cd_withdrawal(clnt_id,wd_amt):
    cd_withdrawal = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_withdrawal where clnt_id={} and wd_amt={}  ".format(clnt_id,wd_amt))
    return cd_withdrawal

#通过交易证券账号和金额查询入金申请单号
def  cd_deposit(clnt_id,dep_amt):
    cd_deposit = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_deposit where clnt_id={} and dep_amt={} ORDER BY init_time DESC  limit 1; ".format(clnt_id,dep_amt))
    return cd_deposit

#查询当前流程状态
def  gs_wrkflw_log(apply_id):
    gs_wrkflw_log = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from gs_wrkflw_log where apply_id={} ORDER BY init_time DESC  limit 1;".format(apply_id))
    return gs_wrkflw_log


#获取当前最新的汇率
def  get_newrate():
    gs_wrkflw_log=SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_exch_rate ORDER BY init_time DESC LIMIT 1;")
    return gs_wrkflw_log


#根据手机号码查询账户申请后的clnt_id
def  get_clnt_id(phone_no):
    clnt_id=SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_ac where clnt_id =(select clnt_id from cd_clnt_apply_basisinfo WHERE apply_id=(select apply_id from cd_clnt_apply_info WHERE phone_no={})) LIMIT 1".format(phone_no))
    return clnt_id


#根据ac_id查询状态交易账户信息
def  cd_ac_id(ac_id):
    cd_ac_id = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_ac WHERE ac_id={}".format(ac_id))
    return cd_ac_id

#其他交易账户申请审批单
def  cd_ac_trading_apply(clnt_id):
    cd_ac_trading_apply = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_ac_trading_apply WHERE clnt_id={}".format(clnt_id))
    return cd_ac_trading_apply

#添加银行卡申请审批单
def  cd_clnt_bank_ac_apply(clnt_id):
    cd_clnt_bank_ac_apply = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_clnt_bank_ac_apply WHERE clnt_id={} ORDER BY init_time DESC LIMIT 1 ".format(clnt_id))
    return cd_clnt_bank_ac_apply

#记录添加银行卡记录
def  cd_clnt_bank_ac(clnt_id):
    cd_clnt_bank_ac = SQL_Check.eddid_gfss_sit(database=sqldata,
                                     sql="select * from cd_clnt_bank_ac WHERE clnt_id={} ORDER BY init_time DESC LIMIT 1 ".format(clnt_id))
    return cd_clnt_bank_ac

if __name__=="__main__":
    # a=cd_ac('NORMAL','CASH','EQUITIES',11431)
    # print(a)
    print(cd_enty(10113278326))
    # print("cd_enty:::",cd_enty(16847802102)[0][4])
    # print("cd_clnt_apply_info:::",cd_clnt_apply_info(16847802102)[0][0])
    # print("cd_enty2:::",cd_enty(16847802102)[0][0])
    # print("cd_clnt_joint_enty:::",cd_clnt_joint_enty(cd_enty(16847802102)[0][0])[0][1])
    # print("cd_ac:::", cd_ac(cd_clnt_joint_enty(cd_enty(16847802102)[0][0])[0][1])[0][0])
    print("cd_clnt:::", cd_clnt(500533)[0][3])
    # print("cd_ac:::1111",cd_ac(11431))
    # print("cd_withdrawal",cd_withdrawal(12071,14.45))
    # print("gs_wrkflw_log",gs_wrkflw_log(52155))
    # print("gs_wrkflw_log",gs_wrkflw_log(52154))
    # print("get_newrate",get_newrate())
    # print("cd_deposit++++++++++++++",cd_deposit(11431,46.41))
    # print("get_clnt_id:",get_clnt_id(13480701220)[0][1])
    # print("get_clnt_id:",get_clnt_id(13480701220))
    # print("cd_ac_id:",cd_ac_id(5007805216))
    print("cd_ac_trading_apply:",cd_ac_trading_apply(88060))
    print("cd_clnt_bank_ac_apply:", cd_clnt_bank_ac_apply(501015))
    print("cd_clnt_bank_ac:", cd_clnt_bank_ac(501015))


