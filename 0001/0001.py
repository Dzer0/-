# coding:utf-8
import random
import string

# zfc = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
# zfc1 = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
# 		'd', 'c', 'b', 'a']
#
# s = []
# for i in range(200):
# 	for q in range(20):
# 		s.append(random.choice(zfc))
# 	yhm = ''.join(s)
#
# #print yhm
# print string.ascii_letters
# print string.digits

# 一下是列表代码
mlc = []
for a in range(200):
	mlc.append(''.join(random.sample((string.ascii_letters + string.digits), 20)))

print mlc

# 下面是字典代码
two = {}
a = 0
for m in range(200):
	a = a + 1
	m = ''.join(random.sample((string.ascii_letters + string.digits), 20))
	two[a] = m

print two
