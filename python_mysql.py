# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:20:22 2021

@author: Administrator
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:58:38 2021

@author: Administrator
"""
import pandas as pd
# 为了兼容mysqldb，只需要加入
import pymysql
pymysql.install_as_MySQLdb()
db = pymysql.connect(host='192.168.3.133', user='root', passwd="12345678", db='data_analysis')
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
cursor.execute("SELECT VERSION()")

data = cursor.fetchone() 

data = pd.DataFrame({'first_name':['wencky','stany','barbio'],
                     'last_name':['wencky','stany','barbio'],
                      'age':[29,29,3],
                      'sex':['w','m','m'],
                      'income':[1000,3000,6000]})

cur = db.cursor()  # 获取一个游标
for i in range(0, 3):
    FIRST_NAME = data["first_name"][i]
    LAST_NAME = data["last_name"][i]
    AGE = data["age"][i]
    SEX=data["sex"][i]
    INCOME=data["income"][i]
        # print("%s,%s,%s" % (zbl_id,zbl_name,zbl_gender))
        # sql = "insert student VALUES (id='%s',name='%s',gender='%s')" % (zbl_id,zbl_name,zbl_gender)
    sql = "insert EMPLOYEE VALUES ('%s','%s','%i','%s',%f)" % (FIRST_NAME, LAST_NAME, AGE ,SEX,INCOME)
        # print(sql)
    cur.execute(sql)
    db.commit()# 将数据写入数据库
db.close()
