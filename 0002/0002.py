# coding:utf-8
# 下面是字典代码
import random, string, MySQLdb


def dict():  # 生成200个优惠码
	two = {}
	a = 0
	for m in range(200):
		a = a + 1
		m = ''.join(random.sample((string.ascii_letters + string.digits), 20))
		two[a] = m  # 字典的添加方式 a[key]=value  具体显示如下: a= {key:'value'}

	return two


# 以下开始连接数据库
# db = MySQLdb.connect(host='localhost', user='root', passwd='', db='test')
db = MySQLdb.connect('localhost', 'root', '', 'test')
cursor = db.cursor()
two = dict()
print two
a = 0
for i in range(200):
	a = a + 1
	yhm = two[a]
	sql = 'insert into yh(yhm) values("%s")' % yhm
	print sql
	cursor.execute(sql)
	db.autocommit(1)
db.close()
