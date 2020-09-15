#---------------------- Bài 10 -------------------------
a = 'zendy - Developer'
# b = a.capitalize() # viết hoa chữ đầu
# b = a.upper() # viết hoa toàn bộ
# b = a.lower() # viết thường toàn bộ
# b = a.swapcase() # chữ thường thành chữ hoa, chữ hoa thành chữ thường
b = a.title() # chữ theo kiểu title, viết hoa chữ đầu tiên Zendy - Developer
print('a: ', a)
print('b: ', b)

c = 'Zendy'
# d = c.center(30) # lấy 30 khoảng và đưa chuỗi vào giữa
d = c.center(30, '-') # center(width, [fillchar]), fillchar là chuỗi có độ dài là 1
print("d: ", d)

e = c.rjust(20, '-') # căn phải
print("e: ", e)
f = c.ljust(25, '*') # căn trái
print('f: ', f)

# g = c.encode(encoding='utf-8', errors='strict') # mã hoá theo chuẩn
g = c.encode() # mã hoá theo chuẩn
print('g: ', g)

h = 'lập trình viên'
i = h.join(['1', '2', '3', '4']) # hoặc h.join(('1', '2', '3', '4'))
print('i: ', i) # 1lập trình viên2lập trình viên3lập trình viên4

k = h.replace('l', 'm') # thay thế chuỗi
print('k: ', k) # mập trình viên

l = h.replace('n', 'zendy', 2) # nếu là 1 sẽ thay chữ n đầu tiên là zendy, nếu là 2 thì sẽ cả 2 chữ n thành zendy
print('l: ', l)

i = 'lblap trinh vienlbl'
k = h.strip('lb') # cắt đi kí tự ở 2 đầu
# k = h.rstrip('lb') # cắt đi phía bên phải
# k = h.lstrip('lb') # cắt đi phía bên trái
print('k: ', k) # ập trình viên


#---------------------- Bài 11 -------------------------
m = 'zendy is frontend developer'
n = m.split(' ') # cắt chuỗi gặp khoảng trắng cho vô 1 mảng
o = m.split('e') # cắt chuỗi gặp chữ e cho vô 1 mảng
p = m.split('e', 2) # cắt chuỗi gặp chữ e chỉ cắt 2 phần chữ em còn lại không cho vô 1 mảng
# q = m.rsplit(' ', 2) # cắt chuỗi gặp khoảng trắng từ phải qua
# r = m.lsplit(' ', 2) # cắt chuỗi gặp khoảng trắng từ trái qua
print('m: ', m)
print('n: ', n) # ['zendy', 'is', 'frontend', 'developer']
print('o: ', o) # ['z', 'ndy is front', 'nd d', 'v', 'lop', 'r']
print('p: ', p) # ['z', 'ndy is front', 'nd developer']

s = m.partition('is') # cắt chuỗi gặp chữ is chia đổi ra tạo ra turple
print('s: ', s) # ('zendy ', 'is', ' frontend developer')

t = m.rpartition('y')
print('t: ', t) # ('zend', 'y', ' is frontend developer')

u = m.count('e') # đếm chữ e xuất hiện bao nhiêu lần trong chuỗi
v= m.count('e', 0, 10) # đếm chữ e xuất hiện từ vị trí từ 0 tới 10 bao nhiêu lần trong chuỗi
print('u: ', u)

w = m.startswith('z') # chuỗi này có xuất phát bằng chữ z không ?
print('w: ', w) # True

x = m.startswith('y', 4, 9) # chữ h có bắt đầu từ vị trí 6 tới 9 hay không
print('x: ', x)

x1 = m.endswith('r') # chữ r có phải là chữ kết thúc của chuỗi
print('x1: ', x1)

x2 = m.find('frontend') # vị trí frontend trong chuỗi nếu không thấy ra -1
# x3 = m.rfind('frontend') # vị trí frontend trong chuỗi
# x4 = m.lfind('frontend') # vị trí frontend trong chuỗi từ trái qua
print('x2: ', x2)

# x5 = m.index('y') # văng lỗi nếu tìm không thấy
# x5 = m.rindex('y') # văng lỗi nếu tìm không thấy
# x5 = m.lindex('y') # văng lỗi nếu tìm không thấy
# print('x5: ', x5)

x6 = m.islower() # chuỗi có phải chuỗi viết thường không
print('x6: ', x6)

x7 = m.isupper()
print('x7: ', x7) # chuỗi có phải toàn bộ viết hoa không

x8 = '5'
x9 = x8.isdigit() # chuỗi có phải là số không
print('x9: ', x9)

x10 = '    '
x11 = x10.isspace() # chuỗi có phải khoảng trắng không
print('x11: ', x11)