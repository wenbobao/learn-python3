import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='demo')
cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# conn.commit()
# cursor.close()

# 查询
sql = r'select goods_id from goods'
cursor.execute(sql)
result = cursor.fetchall()
good_list = []
for item in result:
    good_list.append(item[0])
print(good_list)