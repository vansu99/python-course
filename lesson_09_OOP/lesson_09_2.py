""" Inheritance - Kế thừa là gì?
    - Kế thừa là một tính năng rất mạnh mẽ trong lập trình hướng đối tượng OOP
    - Đề cập đến việc tạo ra một class mới bằng việc ít hoặc không sửa đổi một class đã có.
    class mới được gọi là class dẫn xuất (con), class mà nó kế thừa được gọi là class cơ sở (cha)
    - Cú pháp:
        class BaseClass:
            thân_của_BaseClass
        class DerivedClass(BaseClass):
            thân_của_DerivedClass
    - class dẫn xuất thừa hưởng toàn bộ từ class cơ sở, và có thể được thêm các tính năng mới => Khả năng tái sử dụng code
"""
# Ví dụ về kế thừa

class DaGiac:
    """ class mô tả về đa giác là hình kín, có từ 3 cạnh trở lên,
        thuộc tính n - lưu số cạnh,
        thuộc tính sides - lưu độ dài các cạnh
        phương thức input_sides - yêu cầu người dùng nhập độ dài các cạnh
        phương thức display - hiển thị độ dài các cạnh
        phương thức perimeter - tính và hiển thị chu vi
    """
    def __init__(self, no_sides):
        self.n = no_sides
        self.sides = [0 for i in range(no_sides)]

    def input_sides(self):
        self.sides = [float(input('Nhập cạnh ' + str(i+1) + ': ')) for i in range(self.n)]

    def display(self):
        for i in range(self.n):
            print(f'Side {str(i+1)} is {self.sides[i]}')

    def perimeter(self):
        print(f'Chu vi là {sum(self.sides)}')


import math


class TamGiac(DaGiac):
    """ class mô tả về tam giác, kế thừa từ đa giác
        có thêm phương thức area để tính diện tích của nó
    """

    def __init__(self):
        DaGiac.__init__(self, 3)

    def area(self):
        a, b, c = self.sides
        p = (a + b + c)/2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Diện tích của Tam giác là: %0.5f' % area)


tamgiac = TamGiac()
tamgiac.input_sides()
tamgiac.display()
tamgiac.perimeter()
tamgiac.area()

# Không định nghĩa phương thức input_sides(), display(), perimeter() cho class TamGiac nhưng vẫn có thể dùng bình thường
# Khi 1 thuộc tính không có trong class, sẽ tìm kiếm lên class cơ sở, và cứ thế tiếp tục nếu như class cơ sở là dẫn xuất của class khác


""" Method Overriding - Ghi đè phương thức
    - Trong chương trình trên thấy, __init__() được định nghĩa trong cả 2 class.
    - Điều gì xảy ra, khi method trong class dẫn xuất ghi đề lên class cơ sở
    => __init__() trong lớp dẫn xuất được ưu tiên hơn trong class cơ sở
    - Khi ghi đè, thường chúng ta mong muốn mở rộng nó chứ không đơn thuần là thay thế nó.
    Điều tương tự cũng được thực hiện khi gọi phương thức class cơ sở từ trong class dẫn xuất DaGiac.__init__(self, 3) từ __init__() của TamGiac
    Một cách tốt hơn làm việc này là dùng super()
            DaGiac.__init__(self, 3)  <=>  super().__init__(3)
    - Python cung cấp isinstance() và issubclass() để kiểm tra tính kế thừa
    isinstance() - trả lại True nếu object là thể hiện của class hoặc của class dẫn xuất từ nó.
                   Tất cả các class trong Python đều được kế thừa từ class có tên là object
    issubclass() - kiểm tra kế thừa của 2 class
"""

print(isinstance(tamgiac, TamGiac))
print(isinstance(tamgiac, DaGiac))
print(isinstance(tamgiac, int))
print(isinstance(tamgiac, object))

print(issubclass(TamGiac, DaGiac))
print(issubclass(DaGiac, TamGiac))
print(issubclass(bool, int))


""" Đa kế thừa - Multiple Inheritance
    - Giống như một số ngôn ngữ lập trình khác (như C++, ...), Python cung cấp đa kế thừa
    - Một class có thể được kế thừa từ nhiều class cơ sở
    - Tất cả các thứ của các lớp cơ sở đều kế thừa lại cho class dẫn xuất
    - Cú pháp:
        class Base1:
            thân_của_Base1
        class Base2:
            thân_của_Base2
        class MultiDerived(Base1, Base2):
            thân_của_MultiDerived
"""

""" Kế thừa đa cấp - Multilevel Inheritance
    - Có thể dùng kế thừa từ một lớp dẫn xuất => kế thừa đa cấp. Trong Python, độ sâu bao nhiêu cũng được
    - Trong kế thừa đa cấp, toàn bộ trong class cơ sở và class dẫn xuất được kế thừa lại cho class dẫn xuất mới
    - Cú pháp:
        class Base:
            thân_của_Base
        class Derived1(Base):
            thân_của_Derived1
        class Derived2(Derived1):
            thân_của_Derived2
"""

""" Thứ tự các Resolution
    - Mọi class trong Python đều kế thừa từ class object - đây là class cơ sở nhất
    - Về mặt kỹ thuật, tất cả các class (kể cả dựng sẵn hay do người dùng định nghĩa) đều là class dẫn xuất của class object,
    và tất cả các đối tượng đều là thể hiện của class object => Ví dụ dưới
    - Trong kích bản đa kế thừa, bất kì thuộc tính nào đầu tiên cũng được tìm kiếm tại class hiện tại, nếu không thấy,
    sẽ tìm kiếm lên các lớp cha theo độ ưu tiên: chiều sâu - trước rồi từ trái qua phải, đảm bảo ko tìm kiếm cùng 1 class 2 lần
    Ví dụ: MultiDerived được tìm kiếm theo thứ tự [Base1, Base2, object] - tuyến tính hóa của class MultiDerived,
    quy tắc ngày được gọi là Method Resolution Order (MRO) - Thứ tự phân giải phương thức
    - MRO đảm bảo 1 class luôn xuất hiện trước cha của nó. Được hiển thị bằng thuộc tính __mro__ hoặc phương thức mro() => Ví dụ dưới
"""

print(issubclass(list, object))
print(isinstance(1992, object))
print(isinstance("Python", object))


class Base1:
    pass


class Base2:
    pass


class MultiDerived(Base1, Base2):
    pass


print(MultiDerived.__mro__)
print(MultiDerived.mro())

""" Một ví dụ phức tạp hơn 1 chút cho MRO - hình diễn giải: mro.jpg """

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())