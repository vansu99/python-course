""" Dictionary:
    - Introduction
    - Accessing dict
    - Working with dict
    - Properties
    - Functions and Methods
"""

""" Dictionary là gì?
    - Là tập hợp các phần tử không có thứ tự
    - Mỗi phần tử có dạng cặp key: value
    - Khi biết key có thể truy xuất ra value
"""

""" Làm thế nào để tạo ra một dict?
    - Đặt các phần tử trong cặp ngoặc nhọn {}, cách nhau bởi dấu phẩy
    - Mỗi phần tử có key và value được biểu thị dưới dạng key: value
    - value có thể mang bất kì kiểu dữ liệu nào và có thể trùng lặp;
    còn key thì chỉ được dùng kiểu dữ liệu bất biến (string, number hoặc tuple với các phần tử bất biến) và không lặp
"""
empty_dict = {}  # dict rỗng
print(empty_dict)

my_dict = {
    1: 'Một',
    2: 'Hai',
    3: 'Ba',
}  # dict với key là số nguyên
print(my_dict)

your_dict = {
    'name': 'Python',
    1: [9, 9.5, 6, 7.5, 5]
}  # dict hỗn hợp key
print(your_dict)

our_dict = dict({
    'a': ['apple', 'atime'],
    'f': ['fuk', 'fake'],
    'd': ['dog', 'duck']
})  # dùng dict()
print(our_dict)

a_dict = dict([(1, 'ios'), (2, 'android'), (3, 'winphone')])
print(a_dict)


""" Truy cập vào dict
    - Các kiểu dữ liệu trước đây, nếu có thể thì dùng chỉ số để truy cập
    - Còn dict thì dùng key để truy cập
    - Có thể dùng toán tử [] hoặc hàm get()
    - get() sẽ trả lại None nếu như key ko tồn tại, còn [] sẽ trả lại lỗi: KeyError
"""

my_dict = {
    'name': 'Python',
    'level': 'high',
    'age': 30
}
print(my_dict)
print(my_dict['name'])
print(my_dict.get('age'))

print(my_dict.get('phone'))  # None
print(my_dict['phone'])  # Lỗi: KeyError: 'phone'

""" Thay đổi hoặc thêm mới phần tử:
    - dict là kiểu không bất biến
    - Có thể thêm mới hoặc thay đổi giá trị của phần tử đã tồn tại bằng toán tử gán (=)
    - Nếu key đã tồn tại thì value được cập nhật, ngược lại thì thêm cặp key: value mới
"""
my_dict = {
    'name': 'Duck',
    'age': 2
}
my_dict['age'] += 1  # cập nhật, tăng giá trị của age lên 1 => age = 3
print(my_dict)

my_dict['phone'] = '0912612345'  # thêm phần tử mới
print(my_dict)

my_dict['phone'] = '0987654321'  # cập nhật value cho key phone, vì key này đã tồn tại
print(my_dict)

""" Xóa phần tử:
    - Có thể xóa một phần tử cụ thể bằng cách dùng pop(key), xóa khỏi dict phần tử có key và trả lại value của phần tử đó
    - popitem() dùng để xóa và trả về cặp (key, value) bất kỳ từ dict
    - clear() dùng để xóa toàn bộ các phần tử, biến thành dict rỗng
    - Toán tử del để xóa phần tử cụ thể nào đó
"""
my_dict = {
    1: -1, 2: -2, 3: -3, 4: -4, 0: 0
}
print(my_dict.pop(3))
print(my_dict)

print(my_dict.popitem())
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict
# print(my_dict)  # Lỗi: vì sau del kia sẽ ko còn my_dict nữa


""" Các phương thức của dict
    - clear(): Xóa toàn bộ phần tử, thành dict rỗng
    - copy(): Tạo bản sao cho dict
    - fromkeys(seq[, v]): Trả lại dict mới với các key từ seq và giá trị từ v, nếu không có thì mặc định = None
    - get(key[,d]): Trả lại value của key, nếu key ko tồn tại thì trả lại d, nếu ko có d thì trả lại None
    - items(): Trả lại thể hiện của dict dạng (key, value)
    - keys(): Trả lại List các key của dict
    - pop(key[,d]): Xóa và trả lại value của phần tử có key, nếu không tồn tại key thì trả lại d, nếu ko có d thì báo lỗi KeyError
    - popitem(): Trả lại phần tử bất kì dạng (key, value), nếu dict rỗng thì báo lỗi KeyError
    - setdefault(key[,d]): Nếu key tồn tại, trả lại value, nếu ko thêm key với value=d và trả lại d, nếu ko có d thì là None
    - update([other]): Cập nhật dict với các cặp key-value trong other, nếu key tồn tại thì sẽ ghi đè
    - values(): Trả lại list các giá trị của các phần tử trong dict
"""

# Code lại đoạn chương trình sau và xem kết quả có giống như mô tả về các phương thức bên trên ko!
my_dict = {}.fromkeys([1, 3, 5, 2], 'xk')  # Khai báo my_dict từ tập key, với giá trị mặc định = 'xk'
print("My dict:", my_dict)

my_dict = {1: 4, 2: 5, 3: 6}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for item in my_dict.items():
    print(item)

# Lấy key ra và sắp xếp
print(sorted(my_dict.keys()))

my_dict.update({
    1: 1000,
    4: '4000'
})  # cập nhật giá trị cho key = 1 và thêm mới (key = 4, value = '4000')
print(my_dict)

print("Test phương thức setdefault", my_dict.setdefault(0))
print(my_dict)


""" Dictionary Comprehension: Tạo dict một cách bao quát
    - Tạo dict mới từ việc duyệt lặp
    - Dạng lệnh: cặp key:value theo sau là for, tất cả đc đặt trong {}
    - Trong for có thể chứa nhiều for khác hoặc chứa if
"""

# Cách bình thường tạo như sau:
new_dict = {}
for i in range(10):
    new_dict[i] = (i+1)**2
# => Cách Comprehension
new_dict = {i: (i+1)**2 for i in range(10)}
print(new_dict)

new_dict = {i: (i+1)**2 for i in range(10) if i % 3 == 0}
print(new_dict)


""" Các toán tử khác làm việc với dict
    - in: kiểm tra xem key có trong dict hay ko
    - not in: kiểm tra xem key đó ko có trong dict
    - for và in để duyệt dict
"""
my_dict = {1: 1, 2: 2, 3: 3}
print(1 in my_dict)
print(9 not in my_dict)


for i in my_dict:  # duyệt như này sẽ là duyệt key
    print(f"Key: {i}, value: {my_dict[i]}")

for key in my_dict.keys():
    print(f"Key: {key}, value: {my_dict[key]}")

""" Các phương thức dựng sẵn làm việc với dict
    - all(): Trả lại True nếu các key trong dict là true, hoặc là dict rỗng
    - any(): Trả lại True nếu có bất kì key nào đó true, nếu dict rỗng thì trả lại False
    - len(): Trả lại số lượng phần tử trong dict
    - sorted(): Trả lại một list đã sắp xếp của các key
"""
# Hãy viết chương trình để kiểm chứng lại hoạt động của các hàm trên

my_dict = {1: 2, 0: 3, 4: 5}
print(sorted(my_dict))

a_contact = {
    'first_name': 'Pham',
    'last_name': 'Hoan',
    'cell': '0912614123',
    'home': '0362286624',
    'address': 'Ha Noi',
    'company': 'Teko'
}

my_dict = {
    1: ['a', 'b'],
    2: [2, 4, 6, 5],
    3: {1: 1, 2: 2},
    (1, 2): 10
}
print(my_dict)
