# import json
# import operator
import pymysql

class SQL_Check():
    # 账户中心数据库连接
    def coonect_db_zh(self,database, sql, charset='utf8'):

        conn = pymysql.connect(host="rm-wz94r73is5gxn6it59o.mysql.rds.aliyuncs.com", port=3306, user="eddid_dev",
                               passwd="eddid@123",
                               db=database, charset='utf8')
        cur = conn.cursor()
        try:
            cur.execute(sql)  # 执行sql语句
        except Exception as e:
            conn.rollback()  # 事务回滚
            print("事务处理失败", e)
        else:
            conn.commit()  # 提交事务
            print('事务处理成功', cur.rowcount)
        results = cur.fetchall()
        return results

    "CMDS SIT数据库"
    def get_cdmsdb_con(self,database,sql,chartset='utf-8'):

        self.conn = pymysql.connect(host="192.168.57.25", port=3306, user="devsit", passwd="devSIT2021pwd",
                                    db=database, charset='utf8')
        self.cur=self.conn.cursor()
        try:
            self.cur.execute(sql)#执行sql语句
        except Exception as e:
            # logging.error('sql执行失败，执行语句为:%s'%str(sql))
            self.conn.rollback()# 事务回滚
            print("事务处理失败",e)
        else:
            self.conn.commit()#提交事务
            print('事务处理成功', self.cur.rowcount)
        results=self.cur.fetchall()
        return results


    def eddid_gfss_sit(self,database,sql,chartset='utf-8'):

        self.conn = pymysql.connect(host="192.168.57.25", port=3306, user="devsit", passwd="devSIT2021pwd",
                                    db=database, charset='utf8')
        self.cur=self.conn.cursor()
        try:
            self.cur.execute(sql)#执行sql语句
        except Exception as e:
            # logging.error('sql执行失败，执行语句为:%s'%str(sql))
            self.conn.rollback()# 事务回滚
            print("事务处理失败",e)
        else:
            self.conn.commit()#提交事务
            print('事务处理成功', self.cur.rowcount)
        results=self.cur.fetchall()
        return results
