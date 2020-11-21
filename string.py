print('------------------ Bài 7 -------------------');

test = 'Zendy'

print("test: ", test);

print('------------------ Bài 8 -------------------');

print(r'Test \nhanh');

a = 'Learning'
b = 'Python'
c = a + '\n' + b
print("c: ", c)

d = a*5
print("d: ", d)

#in - nếu chuỗi b nằm trong a thì true
e = b in a;
print("e: ", e) #false

#kiểm tra kí tự ở vị trí index
f = a[2]
print(f) #a

g=a[len(a) -1] #lấy ra kí tự cuối cùng trong dấu ngoặc tròn, len là biểu thức độ dài
print("g: ", g)

#cắt chuỗi
h = a[1:len(a)] #cắt chuỗi từ vị trí nào
i = a[1:None] #từ 1 tới cuối cùng
uu = a[None: 5] #từ đầu tới vị trí index 4: Learn
i = a[None:None] #lấy cả chuỗi
k= a[:]
l = a[None:5:] #bước nhảy từ vị trí 0 tới vị trí index 4 (lấy 5 kí tự)
m = a[None:5:-1] #nhảy ngược lại từ vị trí số 1 ngược lại của chuỗi
print("h: ", h) #earning


v1 = int("69") + 5 #float("6.9") + 5
v2 = str(69) + "5"
print("v1: ", v1)
print("v2: ", v2)
#int("6.9") = 6

strA = "HowKteam.com"
strB = strA[None:1] + "0" + strA[2:None]
print(hash(strB))

print('------------------ Bài 9 -------------------');

n = 'My team is %s %s years old' %('1', '2')
print("n:", n);

m = '%s %s'
result = m %('1', '2')
print("m: ", result)

h = '%f' %(3)
print("h: ", h)

i = '%.3f' %(3.9999)
print("i: ", i)

k = '%.f' %(3.5999)
print("k: ", k)

l = f'Zendy'
print("l: ", l)

o = 'Zendy'
result_o = f'{o} - Developer'
print(result_o)

name = 'Zendy'
address = 'HD'
phone = '038817xxxx'
result_info = f'Student: {name}\nAddress: {address}\nPhone: {phone}'
print('infomation: ', result_info)

variable = 'three'
p = f'1: {{one}}, 2: {{two}}, 3: {variable}'
print("p: ", p)

q = 'a: {}, b: {}, c: {}'.format(1, 2, 3)
print("q: ", q)

r = 'a: %d, b: %d, c: %d' %(1, 2, 3)
print("r: ", r)

s = 'a: {1}, b: {2}, c: {0}'.format('one', 'two', 'three')
print("s: ", s)

t = 'only one value: {0}'.format(1, 2)
print("t: ", t)

u = '1: {one}, 2: {two}'.format(one=111, two=222)
print("u: ", u)

# v = '{:^10}'.format('Zendy')
# v = '{:<10}'.format('Zendy')
v = '{:>50}'.format('Zendy')
print('v: ', v)

x = 'My name {:*^50} OK'.format('Zendy')
print("x: ", x)

# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)