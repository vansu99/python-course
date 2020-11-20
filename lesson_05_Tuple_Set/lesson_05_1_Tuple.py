
""" Tuple:
    - Introduction
    - Accessing Tuple
    - Operations
    - Working with Tuple
    - Functions and Methods
"""
""" ==>> Tuple cũng khá giống với List.
    Điều khác duy nhất là: Tuple ko thể thay đổi các phần tử trong nó còn List thì ngược lại.
"""

""" Cách tạo Tuple: Đặt các phần tử trong cặp ngoặc tròn () và cách nhau bởi dấu phẩy
    => Ngoặc tròn có thể được bỏ qua, nhưng mới bắt đầu thì nên tuân thủ đúng điều trên
"""
empty_tuple = ()  # Tuple rỗng
print(empty_tuple)
my_tuple = (-1, 2, 0, 3)  # Tuple chứa các số nguyên
print(my_tuple)
your_tuple = (1, 'Hi', 'Night!', 2.718, 1+3j)  # Tuple chứa phần tử mang nhiều kiểu dữ liệu
print(your_tuple)
our_tuple = (1992, [1, 0, 3, -5], (), ('Py', 'js', 0, 3.14))  # Tuple dạng lồng nhau
print(our_tuple)

# Tạo Tuple không cần dùng cặp ngoặc tròn  => Kỹ thuật Tuple packing
mine_tuple = 'cat', 1999, 'pig', 1996
print(mine_tuple)

# => unpacking
a, b, c, d = mine_tuple
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# Việc tạo một Tuple có 1 phần tử hơi khó khăn chút và dễ bị nhầm lẫn
one_tuple = ('one element')  # có gợi ý từ IDE, và đang hiểu đây là String ko phải Tuple
print(one_tuple)
a_tuple = ('one element', )  # như này mới hiểu là Tuple 1 phần tử, chú ý dấu phẩy
print(a_tuple)
tuple_01 = 'one element',   # đây cũng được hiểu là Tuple 1 phần tử với việc không dùng ngoặc tròn
print(tuple_01)


""" Truy cập vào trong Tuple
    - Bằng chỉ số dương: Dùng toán tử [] và đưa chỉ số phần tử muốn truy cập. Chỉ số bắt đầu từ 0 đến (số phần tử - 1).
    Với Tuple lồng nhau thì dùng chỉ số lồng nhau.
    - Bằng chỉ số âm: Dùng toán tử [] và đưa chỉ số dạng âm của phần tử muốn truy cập.
    Chỉ số âm đánh từ phải sang trái, bắt đầu là -1 cho phần tử cuối cùng, và ngược đến -(số phần tử) cho phần tử đầu tiên
    - Đoạn cắt: Dùng toán tử [] kết hợp với toán tử : để có thể lấy ra 1 đoạn các phần tử của tuple
"""
your_tuple = (1, 'Hi', 'Night!', 2.718, 1+3j)
print(len(your_tuple))  # Số lượng phần tử của your_tuple
print(your_tuple[4])
print(your_tuple[0])

our_tuple = (1992, [1, 0, 3, -5], (), ('Py', 'js', 0, 3.14))
print(our_tuple[1])
print(our_tuple[1][2])
print(our_tuple[3][1])

my_tuple = ('py', 'thon', 'java', 'script', 'Ox', 'Oy')
print(my_tuple[-2])
print(my_tuple[-6])

my_tuple = ('py', 'thon', 'java', 'script', 'Ox', 'Oy')
print(my_tuple[:4])
print(my_tuple[2:])
print(my_tuple[1:4])
print(my_tuple[:-5])


""" Thay đổi, cập nhật Tuple. Không giống như List, Tuple là kiểu dữ liệu không cho phép thay đổi (giống String).
    - Điều này có nghĩa là các phần tử không thể bị thay đổi.
    Nhưng nếu phần tử trong một Tuple lồng mà là dạng dữ liệu có thể thay đổi thì ta có thể thực hiện thay đổi được (<= Khá dị)
    - Có thể thực hiện gán giá trị mới cho biến Tuple cũ (reassignment)
    - Ghép 2 Tuple bằng cách dùng dấu +
    - Nhân 1 Tuple với 1 số nguyên dương n => lặp lại Tuple đó lên n lần
"""

my_tuple = (1992, [1, 0, 3, -5], (26, 10, 1999))
# my_tuple[2] = 2000  # Lỗi: TypeError: 'tuple' object does not support item assignment
my_tuple[1][3] = 5
print(my_tuple)

my_tuple = ('re', 'assignment', 'reassignment')
print(my_tuple)

tuple_01 = (1, 2, 3)
tuple_02 = (4, 5, 6)
tuple_03 = (7, 8, 9)
print(tuple_01 + tuple_02 + tuple_03)
print(tuple_01 * 2)


""" Xóa phần tử Tuple
    - Như trên đã nói, chúng ta ko thể thay đổi các phần tử trong Tuple => không thể xóa phần tử trong Tuple
    - Tuy nhiên, có thể xóa hoàn toàn 1 tuple bằng từ khóa del
"""
my_tuple = (0, 1, 2, 3, 4, 5)
# del my_tuple[3]  # Lỗi: TypeError: 'tuple' object doesn't support item deletion

del my_tuple  # Xóa hoàn toàn tuple đi
# print(my_tuple)  # Lỗi: NameError: name 'my_tuple' is not defined


""" Các phương thức của Tuple
    - Do không phải kiểu dữ liệu có thể thay đổi => add và remove không thể tồn tại trong kiểu dữ liệu Tuple
    - Chỉ còn 1 phương thức
        - tuple.count(element): Đếm số lượng phần tử element trong tuple
        - tuple.index(element): Trả lại chỉ số của phần tử element đầu tiên từ trái sang phải
"""
my_tuple = ('d', 'o', 'g', 'p', 'i', 'g', 'd', 'u', 'c', 'k')
print(my_tuple.count('g'))
print(my_tuple.index('d'))

""" Các toán tử khác của Tuple
    - Kiểm tra có thuộc Tuple hay không: in hoặc not in
    - Duyệt một Tuple với for và in
"""
my_tuple = ('d', 'o', 'g', 'p', 'i', 'g')
print('a' in my_tuple)
print('i' in my_tuple)
print('h' not in my_tuple)

love_tuple = ("HAT", 'MT', 'HNH', 'TH')
for singer in love_tuple:
    print(f"I like {singer}")

for i in range(len(love_tuple)):
    print(f"I like", love_tuple[i])

""" Một số ƯU ĐIỂM của Tuple so với List.
Theo các thứ đã trao đổi, Tuple khá giống với List và chúng thường được sử dụng trong các tình huống tương tự nhau.
Tuy nhiên, vẫn có một số ưu điểm khi sử dụng Tuple so với List như sau:
    - Thường dùng Tuple chứa các phần tử với các kiểu dữ liệu không đồng nhất (khác nhau)
    Còn List chứa các phần tử với kiểu dữ liệu đồng nhất (giống nhau)
    - Tuple là kiểu dữ liệu immutable (bất biến/ko thay đổi được), thì duyệt nó sẽ nhanh hơn List => Tăng cường hiệu năng
    - Tuple có chứa các phần tử immutable, có thể dùng làm key cho dictionary, với List thì không thể
    - Nếu có dữ liệu không được thay đổi, dùng Tuple sẽ đảm bảo được tính chất đó, nó sẽ chống ghi đè
"""
