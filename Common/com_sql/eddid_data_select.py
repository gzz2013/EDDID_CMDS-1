from Common.com_sql.eddid_sit_库链接 import SQL_Check

SQL_Check=SQL_Check()


# 通过phone查询applyid
def cd_clnt_apply_info(phone):
    print("查询申请单的手机号码为为：{}".format(phone))
    apply_id = SQL_Check.eddid_gfss_sit(database="eddid_gfss_sit",
                               sql="select apply_id from cd_clnt_apply_info where phone_no='{}'".format(
                                  phone))
    applyid=apply_id[0][0]
    return applyid

#在cd_ac表查询符合条件的交易账号
def cd_ac(ac_stat, ac_catg, busin_acty_cde, clnt_id):
    # 通过phone查询applyid
    # print("查询申请单的手机号码为为：{}".format(clnt_id))
    ac_id = SQL_Check.eddid_gfss_sit(database="eddid_gfss_sit",
                                     sql="select ac_id from cd_ac WHERE ac_stat='{}' AND ac_catg='{}' AND busin_acty_cde='{}' AND clnt_id='{}'".format(
                                         ac_stat, ac_catg, busin_acty_cde, clnt_id))
    accountId = ac_id[0][0]
    return accountId

#在通过交易证券账号和金额查询换汇申请单号
def cd_exch(clientId,applyAmount):
    apply_id = SQL_Check.eddid_gfss_sit(database="eddid_gfss_sit",
                                     sql="select apply_id applyid from cd_exch WHERE clnt_id='{}' and apply_amt='{}'".format(clientId,applyAmount))
    applyid = apply_id[0][0]
    return applyid

#通过phoen查询注册账户信息
def cd_enty(phone):
    userinformation = SQL_Check.eddid_gfss_sit(database="eddid_gfss_sit",
                                     sql="SELECT * FROM cd_enty WHERE phone='{}'".format(phone))
    return userinformation




if __name__=="__main__":
    # a=cd_ac('NORMAL','CASH','EQUITIES',11431)
    # print(a)
    print(cd_enty(16847802102))
    print(cd_enty(16847802102)[0][4])

