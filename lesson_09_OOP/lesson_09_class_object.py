# OOP - Class và Object

""" class, object là gì?
    - Python là ngôn ngữ lập trình hướng đối tượng. Không giống như ngôn ngữ lập trình hướng thủ tục, trọng tâm là hàm,
    lập trình hướng đối tượng nhận mạnh vào đối tượng - object
    - object đơn giản chỉ là tập các dữ liệu (biến) và các phương thức hoạt động trên dữ liệu đó. class là bản thết kế cho object
    - Ví dụ, class như bản phác thảo (nguyên mẫu) cho một ngồi nhà, trong đó mô tả về sàn, tường, cửa sổ, ...
    Dựa vào đó, để đi xây dựng ngôi nhà - đây chính là object
    Nhiều ngôi nhà có thể được tạo ra từ một bản thiết kế => tạo ra nhiều object từ một class
    Mỗi object được gọi là instance (thể hiện) cho class, việc tạo ra object này còn được gọi là instantiation - khởi tạo
"""

""" Định nghĩa class:
    - Bắt đầu bằng từ khóa class, sau đó là tên của nó
    - Đoạn string đầu tiên được gọi là docstring - mô tả về class. Dù nó là ko bắt buộc, nhưng nên viết nó
    => như Ví dụ 1
    - Một class sẽ tạo ra một không gian cục bộ mới, nơi mà thuộc tính - attribute của nó được định nghĩa.
    Thuộc tính có thể là data hay function
    - Ngoài ra, còn có các thuộc tính đặc biệt được định nghĩa bắt đầu bằng 2 gạch dưới __, ví dụ: __doc__ trả lại docstring của class đó
    - Ngay khi định nghĩa class, thì một class object mới được tạo ra với cùng tên.
    Cái này giúp cho phép truy cập các thuộc tính và khởi tạo đối tượng mới cho class đó => Xem ví dụ 2
"""
# Ví dụ 1:
class MyClass:
    """ This is a docstring. I have created a new class """
    pass


# Ví dụ 2:
class MyClass:
    """ Đây là docstring của MyClass """
    attr = 0

    def func(self):
        print('Hallo!')


print(MyClass.__doc__)
print(MyClass.attr)
print(MyClass.func)


""" Tạo object
    - Mỗi class object dùng để truy cập vào thuộc tính khác nhau
    - Nó cũng có thể dùng để tạo ra các object mới (thể hiện của class). Cách dùng như một lời gọi hàm => Ví dụ 3: Tạo ra
    một object có tên là obj. Có thể truy cập đến các thuộc tính của object bằng cách dùng tên của object đó.
    - Thuộc tính có thể là data hoặc method. Method của một object là các hàm tương ứng của class. Bất kì function object
    nào là thuộc tính của class đều được xác định là một method cho object của class đó.
    Điều này có nghĩa là MyClass.func là một function object (attribute của class), obj.func là method object
"""
# Ví dụ 3:
obj = MyClass()

# Ví dụ 4:
class MyClass:
    """ Đây là docstring của MyClass """
    attr = 0

    def func(self):
        print('Hallo!')


obj = MyClass()
print(MyClass.func)
print(obj.func)
obj.func()  # Gọi hàm func()


# Để ý, trong class, có tham số self trong định nghĩa function, nhưng khi gọi obj.func() lại ko cần tham số => nó vẫn chạy
# Điều này là do, bất cứ khi nào một đối tượng gọi method của nó, chính là sẽ được truyền làm tham số đầu tiên
# Vì vậy, obj.func() được dịch thành MyClass.func(obj)
# => Túm lại thì, việc gọi phương thức với 1 list n tham số là việc gọi hàm tương ứng với list tham số được tạo ra bằng cách
# thêm object trước tham số đầu tiên. Vì vậy, đối số đầu tiên của hàm trong class phải là chính đối tượng đó,
# điều này được gọi là self, có thể dùng từ khác nhưng khuyên chân thành là nên tuân theo quy ước dùng self.
# Giờ thì đã biết đến: class object, instance object, function object, method object (và sự khác nhau giữa chúng)


""" Constructor - Khởi tạo
    - Các hàm trong class mà được bắt đầu bằng __ được gọi là các hàm đặc biệt và chúng mang nghĩa đặc biệt
    - Một trong số chúng cần quan tâm đặc biệt là __init__(). Nó sẽ được gọi khi một đối tượng mới được tạo ra
    => Hàm kiểu này, trong OOP được gọi là Constructor
    - Thương dùng để khởi tạo sẵn cho các thuộc tính
"""

class Fraction:
    def __init__(self, tu=0, mau=1):
        self.tu_so = tu
        self.mau_so = mau

    def show(self):
        print(f'Phân số: {self.tu_so}/{self.mau_so}')


ps1 = Fraction(1, 3)
ps1.show()

ps2 = Fraction(3, 5)
ps2.attr = 7
print(ps2.tu_so, ps2.mau_so, ps2.attr)

print(ps1.attr)  # AttributeError: 'Fraction' object has no attribute 'attr'

# Trong đoạn code trên, định nghĩa một class mới Fraction biểu diễn cho phân số, có hai hàm
# __init__() để khởi tạo các biến tử số và mẫu số, mặc định là 0 và 1
# và show() để hiển thị phân số đúng cách
# Một thứ rất thú vị, thuộc tính của một đối tượng có thể được tạo ra khi đang chạy chương trình.
# Thấy thuộc tính attr của ps2 được tạo ra và được đọc bình thường, còn ps1 thì ko có, cố tính truy cập sẽ báo lỗi


""" Xóa bỏ thuộc tính và đối tượng
    - Bất kì thuộc tính nào của đối tượng cũng có thể bị xóa bỏ đi bất cứ lúc nào bằng cách dùng câu lệnh del => Ví dụ 5
"""

# Ví dụ 5:
ps3 = Fraction(2, 5)
del ps3.mau_so
ps3.show()  # AttributeError: 'Fraction' object has no attribute 'mau_so'

del Fraction.show
ps3.show()  # AttributeError: 'Fraction' object has no attribute 'show'

ps4 = Fraction(5, 9)
del ps4
ps4  # NameError: name 'ps4' is not defined

# Giải thích: xóa bỏ đối tượng, trong thực tế cũng khá phức tạp
# Khi tạo ra ps4 = Fraction(5, 9) một đối tượng của Fraction được tạo ra trong memory và ps4 được gắn với nó
# Trong lệnh, del ps4 cái liên kết gắn đó bị xóa và tên ps4 được xóa bỏ khỏi không gian các tên biến.
# Và đối tượng thì vẫn tồn tại trong memory, khi ko còn tên nào được gắn với nó thì nó sẽ bị hủy tự động
# Việc hủy tự động các đối tượng không có tham chiếu này trong Python được gọi là bộ sưu tập rác - garbage collection