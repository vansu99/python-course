
""" OOPs trong Python
    - Python là một trong những ngôn ngữ lập trình đa mô hình => Python sẽ hỗ trợ nhiều phương pháp lập trình khác nhau
    - Một trong những phương pháp tiếp cận phổ biến hiện nay là Hướng đối tượng - Object-Oriented Programming (OOP)
    - Một đối tượng có hai đặc trưng:
        - Thuộc tính (attributes)
        - Hành vi (behavior)
    - Xét ví dụ sau:
        Cat là một đối tượng có:
        - tên, tuổi, màu lông => Thuộc tính
        - kêu, chạy, nhảy, ăn, uống => Hành vi
    - Khái niệm OOP trong Python còn tập trung vào việc viết code có thể tái sử dụng, được biết đến như là DRY - Dont Repeat Yourself
    - Trong Python, OOP theo một số nguyên tắc cơ bản như sau:
        - Inheritance - Kế thừa: Sử dụng các chi tiết từ một class mới mà ko làm thay đổi gì class đã có
        - Encapsulation - Đóng gói: Ẩn các chi tiết riêng tư của một class đối với các object khác
        - Polymorphism - Đa hình: Sử dụng các thao tác chung theo nhiều cách khác nhau tương ứng với các đầu vào khác nhau
"""

""" Class - Là bản thiết kế cho object
    - Có thể hình dùng class như một bản phác thảo của một cat với các nhãn. Nó chứa tất cả chi tiết về name, age, ...
    - Dựa trên các mô tả đó, chúng ta sẽ đi tìm hiểu về cat, ở đây, cat là một object
"""
class Cat:
    pass
# Sử dụng keyword class để định nghĩa một class Cat - rỗng. Từ class, chúng ta sẽ khởi tạo được instance.
# Một instance là một đối tượng riêng biệt từ lớp cụ thể


""" Object
    - Một object (instance) là một khởi tạo của một lớp
    - Khi class được định nghĩa, thì chỉ có các mô tả của object được xác định
    => không có bộ nhớ hoặc lưu trữ nào được phân bổ
"""
obj_cat = Cat()
# Ở đây, obj_cat là object của class Cat

# Chúng ta đã nói chi tiết về Mèo - Cat rồi, giờ sẽ cũng nhau đi xây dựng chi tiết về class và về object của Cat như sau:
class Cat:
    # class attribute - thuộc tính của class
    loai = 'Thú họ Mèo'

    # instance attribute - thuộc tính của đối tượng
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


# instance of Cat class - Khai báo 2 đối tượng của class Cat
muop = Cat('Mướp', 2, 'Vàng')
mun = Cat('Mun', 1, 'Đen')

# Truy cập class attribute
print(f'Mướp là', muop.__class__.loai)
print(f'Mun cũng là', mun.__class__.loai)

# Truy cập instance attribute
print(f'{muop.name} đã {muop.age} tuổi và lông màu {muop.color}')
print(f'{mun.name} đã {mun.age} tuổi và lông màu {mun.color}')

# Trong đoạn chương trình trên, đã tạo ra một class Cat với các attribute và các attribute là những đặc trưng của từng object
# Sau đó, tạo 2 object của Cat là muop và mun
# Truy cập đến thuộc tính class (class attribute) bằng __class__.loai. Các class attribute sẽ là như nhau với mọi object của Cat
# Truy cập đến instance attribute bằng muop.name, muop.age, ... Các instance attribute của các object sẽ là khác nhau


""" Method - Là các định nghĩa hàm bên trong thân class, dùng để định nghĩa hành vi của object """

# Ví dụ: Tạo method trong Python
class Cat:
    # class attribute - thuộc tính của class
    loai = 'Thú họ Mèo'

    # instance attribute - thuộc tính của đối tượng
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # instance method
    def run(self):
        return f'{self.name} đang chạy'

    def eat(self, f):
        return f'{self.name} thích ăn {f}'


cam = Cat('Cam', 2, 'Vàng, Trắng')

# call instance methods
print(cam.run())
print(cam.eat('pate gan'))

# Ở trên chúng ta định nghĩa 2 method: run() và eat(), đây được gọi là instance method vì chúng chỉ được gọi qua một instance object


""" Inheritance - Kế thừa
    - Là cách tạo ra class mới có sử dụng chi tiết từ class đã có mà ko thay đổi nó
    - Lớp mới được gọi là lớp dẫn xuất (hoặc lớp con), lớp đã có là lớp cơ sở (hoặc lớp cha)
"""
# Ví dụ:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Tạo Person!')

    def who_am_i(self):
        print('Person')

    def speak(self, lang='Tiếng Việt'):
        print(f'{self.name} nói {lang}')


class StudentIT(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        print('Tạo StudentIT!')

    def who_am_i(self):
        print('StudentIT')

    def code(self, lang):
        print(f'{self.name} lập trình {lang}')


svbk = StudentIT('CườngĐM', 30, 'HUST')
svbk.who_am_i()
svbk.speak()
svbk.code('Python')

# Trong đoạn chương trình trên, chúng ta tạo ra 2 class: Person (cha) và StudentIT (con).
# Class con kế thừa toàn bộ các hàm của class cha, có thể nhìn thấy method speak()
# Tiếp đến, class con đã thay đổi hành vi của class cha với method who_am_i()
# Hơn nữa, class con mở rộng class cha với method code()
# Thêm đó, sử dụng super().__init__() vì muốn kéo toàn bộ __init__() của class cha vào class con


""" Encapsulation - Đóng gói
    - Trong Python, có thể hạn chế quyền truy cập vào các phương thức và biến => ngăn dữ liệu ko bị sửa đổi trực tiếp
    => được gọi là Đóng gói - Encapsulation
    - Dùng ký hiệu cho thuộc tính private là 2 gạch dưới __
"""
# Ví dụ
class Laptop:

    def __init__(self):
        self.__price = 500

    def sell(self):
        print(f'Giá bán là {self.__price}')

    def set_price(self, price):
        self.__price = price


lap = Laptop()
lap.sell()

# thay đổi giá trị price, cố tình truy cập vào thuộc tính
lap.__price = 1000
lap.sell()

# thay đổi qua hàm setter
lap.set_price(1000)
lap.sell()

# Trong chương trình trên, khai báo một class Laptop, trong method __init__() lưu giá của laptop đó.
# Cố gắng thay đổi giá, tuy nhiên, ko thể, vì python coi __price là thuộc tính private
# Để thay đổi giá thì ta dùng qua setter: set_price() với tham số là giá mới
# Cách để lấy giá của các thuộc tính ra thì dùng hàm getter, ở đây chính là sell()


""" Polymorphism - Đa hình
    - Là khả năng (trong OOP) cho phép dùng chung interface cho nhiều hình thái (kiểu dữ liệu)
    - Ví dụ cho dễ hiểu: Cần tô màu cho một hình, có nhiều hình: vuông, tròn, chữ nhật, ...; nhưng có thể dùng cùng một
    phương thức để tô màu cho hình => Đây chính là đa hình
"""
# Ví dụ:
class PC:
    def wifi(self):
        print('Không kết nối được!')


class Laptop:
    def wifi(self):
        print('Kết nối được rồi!')


def connect_wifi(computer):
    computer.wifi()


lap = Laptop()
pc = PC()

connect_wifi(lap)
connect_wifi(pc)

# Trong đoạn chương trình trên, tạo 2 class PC và Laptop, mỗi cái đều có method wifi(); tuy nhiên, chúng khác nhau
# Để kiểm tra về đa hình, tạo ra hàm connect_wifi() nhận bất kì object.
# Truyền vào hàm đó đối tượng lap và pc và chạy nó xem kết quả.

""" Lưu ý:
    - Lập trình trở lên dễ dàng và hiệu quả
    - Class có thể chia sẻ, nên code có thể sử dụng lại
    - Năng suất của chương trình tăng
    - Dữ liệu được an toàn và bảo mật với sự trừu tượng hóa dữ liệu
"""