import sqlite3

Cookie_expiry_days = 30
Cookie_name = 'MlStreamlitAuthCookie'
Cookie_key = 'MlStreamlitAuthCookieKey'

static_source = {'class_video': "D:\\dev\\static\\video", 'class_ppt': "D:\\dev\\static\\ppt",
                 'class_notebook': "D:\\dev\\static\\notebook", }

preauthorized_emails = ['qqab13226252203@163.com']

conn = sqlite3.connect('mlst_user.db')

# 创建游标
c = conn.cursor()

test_users = {'usernames': {}
              }

# 转换为字典
for row in c.execute('SELECT * FROM users'):
    test_users['usernames'][row[0]] = {'email': row[1], 'name': row[2], 'password': row[3]}

c.close()

print(f'select {len(test_users["usernames"])} users from database')
