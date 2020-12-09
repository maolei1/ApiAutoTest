'''
数据库的操作
'''
import pymysql

def connect(db):
    '''
    连接数据库
    :param db: 数据库相关的信息
    :return: 连接对象
    '''
    host = db['host']
    port = db['port']
    user = db['user']
    pwd = db['pwd']
    name = db['name']
    try:
        # 连接数据库
       conn = pymysql.connect(host=host,port=port,user=user,password=pwd,
                              database=name,charset='utf8')
       print("数据库连接成功")
       return conn
    except Exception as e:
        print(f"数据库连接失败，异常信息为：{e}")

def disconnect(conn):
    try:
        conn.close()
        print("断开数据库连接成功")
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为：{e}")

def excute(conn,sql,):
    '''
    执行sql语句
    :param conn:  connect返回连接对象
    :param sql: 要执行的sql语句
    :return: 无
    '''
    try:
        c = conn.cursor() #获取游标
        c.execute(sql) #使用游标执行sql语句
        conn.commit() #提交
        c.close() #关闭游标
        print(f"执行sql语句成功：{sql}")
    except Exception as e:
        print(f"执行sql语句失败，异常信息为：{e}")

def excute_cursor(conn,sql):
    '''
    执行sql语句
    :param conn:  connect返回连接对象
    :param sql: 要执行的sql语句
    :return: 无
    '''
    try:
        c = conn.cursor()  # 获取游标
        row_count = c.execute(sql)  # 使用游标执行sql语句
        conn.commit()  # 提交
        a = c.fetchall()
        c.close()  # 关闭游标
        print(f"执行sql语句成功：{sql}")
        return list(a)
    except Exception as e:
        print(f"执行sql语句失败，异常信息为：{e}")

if __name__ == '__main__':
    db = {"host":"jy001","port":4406,"name":"future","user":"root","pwd":"123456"}
    conn = connect(db)
    sql = "delete from member"
    excute(conn,sql)
    disconnect(conn)