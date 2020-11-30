
# tupple không cho phép sửa chữa nội dung như list
# được giới hạn bởi cặp ngoặc ()
# phân cách nhau bởi dấu ,
# tuple có khả năng chứa mọi giá trị
# tốc độ truy xuất tuple nhanh hơn list
# dung lượng chiếm trong bộ nhớ nhỏ hơn list
# bảo vệ dữ liệu không bị thay đổi
# có thể dùng làm key của dictionary

a = (1, 2, 3)

b = (1,)
print('b: ', b) # (1,)

c = tuple([1, 2, 3])
print('c: ', c) # (1, 2, 3)

d = tuple((1, 2, 3))
print('d: ', d) # (1, 2, 3)

e = tuple('Zendy')
print('e: ', e) # ('Z', 'e', 'n', 'd', 'y')

f = (i for i in range(10) if i % 2 == 0)
g = tuple(f)
print(g) # (0, 2, 4, 6, 8)

h = (1, 2, 3)
h += (4, 5, 6)
print('k: ', h) # (1, 2, 3, 4, 5, 6)

i = (1, 2, 3)
i *= 2
print(i) # (1, 2, 3, 1, 2, 3)
k = 1 in i
print('k: ', k) # True
l = i[0]
print('l: ', l) # 1
m = len(i)
print('m: ', m) # 3
n = i[-1]
print('n: ', n) # 3
o = i [::-1]
print('o: ', o) # (3, 2, 1)
m = i.count(1) # 1 xuất hiện bao nhiêu lần
print('m: ', m) # 1
n = i.index(3) # vị trí index xuất hiện đầu tiên của 3
print('n: ', n) # 2


