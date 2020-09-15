# ----------------- Bài 12 ------------------

a = [i for i in range(30)]
print('a: ', a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


b = [[n, n*1, n*2] for n in range(1,4)]
print('b: ', b) # [[1, 1, 2], [2, 2, 4], [3, 3, 6]]


c = list('zendy')
print('c: ', c) # ['z', 'e', 'n', 'd', 'y']


d = [1, 2]
d+= ['zendy', 'developer'] # d = d + ['zendy', 'developer']
print('d: ', d) # [1, 2, 'zendy', 'developer']


e = [1, 2]
e*= 2
print('e: ', e) # [1, 2, 1, 2]


f = [1, 2]
g = 1 in f # 1 có nằm trong f không
print('g: ', g) # True


h = [1, 2, 3, 'zendy', 'developer', [3, 4]]
i = h[2]
k = h[5][1]
n = h[-1]
m = h[1: 4] # lấy giá trị index của 1, 2, 3
o = h[:2] # lấy giá trị index của 0, 1
p = h[::-1] # lấy và đảo ngược lại mảng
print('i: ', i) # 3
print('k: ', k) # 4
print('n: ', n) # [3, 4]
print('m: ', m) # [2, 3, 'zendy']
print('o: ', o) # [1, 2]
print('p: ', p) # [[3, 4], 'developer', 'zendy', 3, 2, 1]


q = [1, 2, 3, 'zendy', 'developer', [3, 4]]
q[1] = 'frontend'
print('q: ', q) # [1, 'frontend', 3, 'zendy', 'developer', [3, 4]]



r = [1, 2, 3]
s = list(r) # copy r
s[0] = 4
print('r: ', r) # [1, 2, 3]
print('s: ', s) #  [4, 2, 3]


t = [[1, 2, 3], [4, 5, 6]]
u = list(t) # cho dù gán list bên trong ma trận thì giá trị vẫn thay đổi theo trừ u[0] = 'zendy'
u[0][0] = 'zendy'
print('t: ', t) # [['zendy', 2, 3], [4, 5, 6]]
print('u: ', u) # [['zendy', 2, 3], [4, 5, 6]]

