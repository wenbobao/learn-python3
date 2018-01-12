import requests
import mysql.connector
 
conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()
# cursor.execute('create table goods (id varchar(20) primary key, title varchar(200), price varchar(200))')

params = {'type': 'total', 'appkey': '', 'v' : '2', 'page' : '1'} 
r = requests.get('http://api.dataoke.com/index.php?r=Port/index', params=params)
items = r.json()['result'];
print(items)

for item in items:
  cursor.execute('insert into goods (id, title, price) values (%s, %s, %s)', [ item['ID'], item['Title'], item['Price']])
  conn.commit()

cursor.close()