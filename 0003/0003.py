# coding:utf-8
import redis, random, string

# 一下是列表代码
mlc = []
for a in range(200):  # 循环200次
	mlc.append(''.join(random.sample((string.ascii_letters + string.digits), 20)))

print mlc[0]

r = redis.Redis('localhost', 6379, 0)
i = 0
for i in range(200):
	r.lpush('Mykey01', mlc[i])
	i = i + 1

print r.lrange('Mykey01', 0, -1)
r.save()
