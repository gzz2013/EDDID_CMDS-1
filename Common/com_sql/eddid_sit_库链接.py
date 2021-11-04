# import json
# import operator
import pymysql
from Config.cdms_config import *
from sshtunnel import SSHTunnelForwarder

class SQL_Check():

    sqlhost=eddid_gfss_host
    sqlport=eddid_gfss_port
    sqluser=eddid_gfss_user
    sqlpasswd=eddid_gfss_passwd
    shhhost=eddid_gfss_shhhost
    shhport=eddid_gfss_shhport
    shhuser=eddid_gfss_shhuser
    shhpasswd=eddid_gfss_shhpasswd

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

        print("+++++++++++++++++++++++++++获取到数据库的信息database={},host={}，port={}，user={}，passwd={}".format(database,eddid_gfss_host,eddid_gfss_port,eddid_gfss_user,eddid_gfss_passwd))
        if database=="eddid_gfss_uat":
            with SSHTunnelForwarder(
                ssh_address_or_host=(eddid_gfss_shhhost, eddid_gfss_shhport),  # ssh 目标服务器 ip 和 port
                ssh_username=eddid_gfss_shhuser,  # ssh 目标服务器用户名
                ssh_password=eddid_gfss_shhpasswd,  # ssh 目标服务器用户密码
                remote_bind_address=(eddid_gfss_host, eddid_gfss_port),  # mysql 服务ip 和 part
                local_bind_address=('127.0.0.1', 5143)  # ssh 目标服务器的用于连接 mysql 或 redis 的端口，该 ip 必须为 127.0.0.1
            ) as server:
                self.conn = pymysql.connect(
                    host=server.local_bind_host,  # server.local_bind_host 是 参数 local_bind_address 的 ip
                    port=server.local_bind_port,  # server.local_bind_host 是 参数 local_bind_address 的 port
                    user=eddid_gfss_user,
                    password=eddid_gfss_passwd,
                    db=database,
                    charset="utf8"
                )
                self.cur = self.conn.cursor()
                try:
                    self.cur.execute(sql)  # 执行sql语句
                except Exception as e:
                    # logging.error('sql执行失败，执行语句为:%s'%str(sql))
                    self.conn.rollback()  # 事务回滚
                    print("事务处理失败", e)
                else:
                    self.conn.commit()  # 提交事务
                    print('事务处理成功', self.cur.rowcount)
                results = self.cur.fetchall()
                return results
        else:
            self.conn = pymysql.connect(host=eddid_gfss_host, port=eddid_gfss_port, user=eddid_gfss_user, passwd=eddid_gfss_passwd,
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



