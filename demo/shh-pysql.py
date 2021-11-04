import pymysql
from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(
        ssh_address_or_host=('192.168.57.20', 22),  # ssh 目标服务器 ip 和 port
        ssh_username="dev",  # ssh 目标服务器用户名
        # ssh_username="admin",
        ssh_password= "dev2021DEV",           # ssh 目标服务器用户密码
        # ssh_password="9$96f#b4tZy5m",
        # ssh_pkey="C:\\Users\\Administrator\\.ssh\\id_rsa",  # ssh 目标服务器证书
        # ssh_private_key_password="",  # ssh 目标服务器证书密码
        remote_bind_address=('192.168.57.113', 3306),  # mysql 服务ip 和 part
        local_bind_address=('127.0.0.1', 5143)  # ssh 目标服务器的用于连接 mysql 或 redis 的端口，该 ip 必须为 127.0.0.1
) as server:
    conn = pymysql.connect(
        host=server.local_bind_host,  # server.local_bind_host 是 参数 local_bind_address 的 ip
        port=server.local_bind_port,  # server.local_bind_host 是 参数 local_bind_address 的 port
        user="admin",
        password="9$96f#b4tZy5m",
        db="eddid_gfss_uat",
        charset="utf8"
    )
    cursor = conn.cursor()
    # sql = "SELECT * FROM satel_report WHERE id = 1"
    sql = "select * from cd_ac ORDER BY update_time DESC LIMIT 1"
    try:

        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
    except:
        print("SQL执行失败")