# coding:utf-8
import redis, random, string

# 一下是列表代码
mlc = []
for a in range(200):  # 循环200次
	mlc.append(''.join(random.sample((string.ascii_letters + string.digits), 20)))

print mlc[0]

r = redis.Redis('localhost', 6379, 0)
