""" Introduction
    + History and Features
    + Setting up path
    + Working with Python
    + Basic Syntax
    + Variable and Data Type
    + Operator
"""

""" Môi trường làm việc với Python
    + Offline: Python3.6, PyCharm, Vscode
    + Online: repl.it, ...
"""

# Chương trình đầu tiên: In ra dòng chữ 'Hi! I am Python.'
print("Hi! I am Python.")  # Bấm chuột phải vào đây và chọn Run để chạy chương trình và xem nó in ra như mong muốn ko!


""" Các cách viết comment
    + Comment 1 dòng dùng #
    + Comment nhiều dòng thì dùng # tại mỗi đầu dòng; hoặc dùng cặp 3 nháy đơn hoặc dùng cặp 3 nháy kép
"""

# Nhập đoạn chương trình sau và chạy chương trình để xem kết quả hiện ra
print(4000 + 1000 - 3000)
print(12 * 3 / 4)

""" Giới thiệu về các phép toán số học:
    Phép toán      Ý nghĩa          Ví dụ
        +           Cộng            2 + 3 = 5
        -           Trừ             1 - 10 = -9
        *           Nhân            5 * 8 = 40
        /           Chia            21 / 5 = 4.2
        //      Chia lấy nguyên     21 // 5 = 4
        %       Chia lấy dư         21 % 5 = 1
        **          Lũy thừa        2 ** 3 = 8 (2^3)
"""
# Nhập đoạn chương trình sau và rồi chạy để kiểm tra kết quả
print(2 + 3)
print(1 - 10)
print(5 * 8)
print(21 / 5)
print(21 // 5)
print(21 % 5)
print(2 ** 3)

"""
- Biến - Variable: Một cái tên/nhãn dùng để gọi một giá trị nào đó
- Dùng biến giúp chương trình mạch lạc, dễ hiểu
- Để gán giá trị vào biến ta dùng dấu bằng(=). Ví dụ: year_born = 1980, name = 'Py'
"""
# Nhập đoạn chương trình sau và chạy để kiểm tra kết quả
name = 'Python'
print(name + ' was born in')
year_born = 1980
print(year_born)

"""
Quy tắc đặt tên biến:
    - Chỉ gồm chữ cái (a-z, A-Z) hoặc chữ số (0-9) hoặc gạch dưới (_)
    - Không bắt đầu bằng chữ số
    - Không được trùng với từ khóa của ngôn ngữ (bảng từ khóa)
    - Độ dài tùy ý
Ví dụ:
    - Hợp lệ: myClass, var_1, query_set, _products, ...
    - Không hợp lệ: 1_connection, global, class, text!, bien-1...
Lưu ý:
    - Python là ngôn ngữ có phân biệt hoa và thường.
    - Đặt tên biến sao cho có tính gợi nhớ
    - Tên biến gồm nhiều từ thì cách nhau bằng gạch dưới
"""
# Sử dụng biến để làm bài sau: Tính trung bình cộng của 3 số đó

a, b, c = 1, 2, 3   # Thực hiện gán các giá trị cho nhiều biến đồng thời
tb = (a + b + c) / 3
print(tb)

# Gán cùng 1 giá trị cho nhiều biến
i = j = k = 0
print(i)
print(j)
print(k)

""" Các kiểu dữ liệu cơ bản:
    + Number: int, float, complex
    + String
    + lists
    + ...
"""
# Nhập chương trình sau và chạy để xem kết quả.
var = 1992
print(var, 'is of type', type(var))
var = 10.26
print(var, 'is of type', type(var))
var = 2 + 1j
print(var, 'is complex number?', isinstance(var, complex))

"""
- Xâu/Chuỗi ký tự là đoạn chữ, trong đó, mỗi thành phần nhỏ gọi là ký tự.
- Thường đặt trong cặp dấu nháy kép hoặc dấu nháy đơn.
- Để khai báo chuỗi có nhiều dòng thì đặt đoạn chữ trong cặp 3 dấu nháy kép hoặc 3 dấu nháy đơn
"""

msg = '''Hồn tôi là một vườn hoa lá
Rất đậm hương và rộn tiếng chim...
- Trích Từ ấy của Tố Hữu -
'''
print(msg)

"""
Trong chuỗi có chứa ký tự đặc biệt là nháy đơn thì có 3 cách để giải quyết
    - Cách 1: Dùng dấu nháy kép
    - Cách 2: Đánh dấu lại bằng backslash (Kỹ thuật: Escape special characters)
    - Cách 3: Dùng cú pháp trên nhiều dòng
Một số ký tự đặc biệt hay thấy: \', \", \n - xuống dòng , \t - dấu tab
"""

s = 'I \'m Python and I \'m great!'
print(s)


""" Kiểu dữ liệu và các phép toán
    + Số nguyên: + - * / % // **
    + Số thực: + - * / **
    + Xâu/Chuỗi: + (nối chuỗi) * (với một số)
"""

s1 = 'Hi.'
s2 = 'How are U?'
s3 = 'I am good. And U?'
print(s1 + s2 + s3)
print(s1 * 10)

# Nhập đoạn chương trình sau và chạy thử để xem kết quả
print(1.0 + 2)  # Ra số thực
print("10" * 5)  # Ra chuỗi
print(25 / 5)  # Ra số thực
print("abc" + "xyz")  # Ra chuỗi
# print("I am " + 20 + " years old.")  # Lỗi: Type Error
print("I am " + str(20) + " years old.")  # Ép kiểu sang string

""" Chuyển đổi kiểu dữ liệu (ép kiểu) - Type Casting
    + Hàm str() chuyển một giá trị thành chuỗi
    + Hàm int() chuyển một giá trị thành số nguyên
    + Hàm float() chuyển một giá trị thành số thực
"""

# Nhập lại đoạn chương trình sau và thêm các hàm để in giá trị các biến ra màn hình
a = str(123456) + "7890"
b = 1 + int(2) + int(3.4)
c = float('1.1') * float(2)


# Nhúng giá trị vào trong chuỗi
name, py = 'Py', "Thon"
print('Xin chao %s. Toi la %s' % (name, py))

x, y = 123, 456
print("Gia tri cua x la {}, y la {} và trung binh la: {}".format(x, y, (x+y)/2))

print("I love {0} and {1}".format('Python', 'JavaScript'))
print("I love {1} and {0}".format('Python', 'JavaScript'))
print("Hello {f_name}. I am {my_name}.".format(f_name='John', my_name='PyCore'))


""" Nhập dữ liệu với hàm input()
    + Gặp lệnh này, chương trình sẽ chờ người dùng nhập vào gì đó và bấm phím Enter
    + Lưu lại giá trị nhập này có thể dùng biến
    + Luôn nhận vào thành 1 chuỗi. Cần thì ép kiểu như phần trước
"""

# Người dùng nhập vào bán kình đường tròn, tính diện tích in ra màn hình
radius = float(input("Nhập bán kính = "))
area = 3.14 * radius ** 2
print("Hình tròn bán kính {} thì diện tích là {}".format(radius, area))

# Cần làm tròn số ta có thể dùng hàm round(value, số_chữ_số_sau_dấu_phẩy)
n, m = 0.123, 0.456
print(round(n + m, 2))  # số_chữ_số_sau_dấu_phẩy có thể âm, thử để cảm nhận


""" Python Import
    - Khi một chương trình ngày càng lớn dần lên, cần chia thành các module khác nhau cho rành mạch, dễ quan sát
    - Một module trong Python là một file .py
    - Để các module gọi được các thành phần bên trong nhau thì ta dùng import
"""
import math

radis = float(input("Nhập bán kính = "))
area = math.pi * radis ** 2
print("Hình tròn bán kình {} thì diện tích là {}".format(radis, round(area, 3)))

import sys
print(sys.path)

""" Một số hàm và hằng số trong module math
    - Hằng số: math.pi, math.e
    - Căn bậc 2: math.sqrt(x)
    - Làm tròn xuống: math.floor(x)
    - Làm tròn lên: math.ceil(x)
    - Bỏ phần thập phân: math.trunc(x)
    - Giai thừa: math.factorial(n)
    - Ước chung lớn nhất: math.gcd(a, b)
    - Lượng giác: math.sin(x), math.cos(x), math.tan(x), math.asin(x), ....
"""

import math
print(math.pi)
print(math.e)
print(math.floor(0.9))
print(math.ceil(1.1))
print(math.trunc(-10.901))
print(math.factorial(3))
print(math.gcd(36, 63))
