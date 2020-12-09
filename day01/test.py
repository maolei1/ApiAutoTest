import pymysql
# 打开数据库连接,localhost是本地，test123,test1分别是用户名和密码，test是库名
db = pymysql.connect("localhost", "root", None,"maolei")
# 连接数据库
cursor = db.cursor()
print("数据库连接成功")
sql = "delete from mao;"
try:
    # 执行sql语句
    cursor.execute(sql)
    # 将结果输出到控制台
    for i in cursor.fetchall():
        print(i)
    # 提交到数据库
    db.commit()
except Exception as e:
    # 回退
    # db.rollback()
    print(e)
# 关闭数据库连接
db.close()