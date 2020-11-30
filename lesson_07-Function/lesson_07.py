""" Function:
    - Defining a function
    - Calling a function
    - Types of function
    - Function arguments
    - Anonymous functions
    - Global and local variables
"""

""" Function (Hàm) là gì?
    - Một function là một nhóm các câu lệnh để hoàn thành một task (nhiệm vụ/chức năng/công việc) nào đó
    - Functions sẽ chia chương trình thành các phần nhỏ
    - Khi chương trình càng ngày càng lớn thì functions giúp chương trình có tính tổ chức và dễ quản lý
    - Hơn cả, function giúp code có thể tái sử dụng và tránh lặp lại
"""

"""
    def function_name(parameters):
        các_câu_lệnh_của_function
Cú pháp khi viết function bao gồm các phần sau:
    - Từ khóa def để đánh dấu bắt đầu của một function header
    - function_name - tên của hàm để xác định được function.
    Việc đặt tên hàm tuân theo các quy tắc viết định danh (như phần đặt tên biến)
    - parameters (arguments) - không hoặc một hoặc nhiều tham số, thông qua đó truyền giá trị cho function (có thể không cần)
    - Dấu hai chấm để đánh dấu kết thúc của function header
    - docstring (có thể không cần) để mô tả function làm gì
    - Một hoặc nhiều câu lệnh tạo lên function body. Các câu lệnh ở cùng mức thụt đầu dòng
    - Có thể có hoặc không câu lệnh return để trả lại giá trị nào đó từ function
"""


def func_greet(name):
    """
    Đây là hàm greet,
    sẽ in ra câu chào hỏi người có tên được truyền vào.
    """
    print(f"Hello {name}. Good evening!")


""" Làm thế nào để call (gọi) một function?
    - Sau khi định nghĩa xong một function, có thể gọi nó từ 1 function khác, một chương trình khác hoặc trong dấu nhắc Python (Python prompt)
    - Để gọi hàm, chỉ cần gõ tên hàm và các tham số của nó (nếu có)
"""

func_greet('Hoan')

""" Docstring viết tắt của documentation string. Để giải thích ngắn gọn những gì function làm
    - Là đoạn string đầu tiên được gọi đến sau tên hàm
    - Đây là một tuỳ chọn, có thể có hoặc không.
    - Việc viết docstring là cách thực hành lập trình tốt nhất
    - Hãy luôn viết docstring cho code của mình, để tránh việc khi đọc lại không nhớ nổi đoạn đó làm gì
    - Dùng cặp dấu nháy kép để viết docstring trên nhiều dòng, và nó sẽ được gán vào thuộc tính __doc__ của function đó
"""
print(func_greet.__doc__)


""" Câu lệnh return:
    - Dùng để kết thúc một function và quay lại nơi nó được gọi
    - Cú pháp:
        return kết_quả_cần_trả_về
    - kết_quả_cần_trả_về có thể là biểu thức, giá trị cần trả về.
    - Nếu không có kết_quả_cần_trả_về hoặc không có câu lệnh return thì function trả lại giá trị None
"""
value_return = func_greet('Yuki Ame')
print(value_return)


def odd_factorial(n):
    """ Ví dụ về function có giá trị trả về.
    Hàm tính tích các số lẻ không vượt quá n
    :param n: limit to be calculated
    :return: product the odd numbers
    """
    result = 1
    for i in range(1, n+1, 2):
        result *= i
    return result


print(odd_factorial(5))
print(odd_factorial(10))


""" Cách hoạt động của function => python-how-function-works.jpg """
""" Phạm vi và Vòng đời của biến
    - Phụ thuộc vào nơi biến được nhận ra
    - Các biến khai báo trong function, sẽ không thể thao tác được từ bên ngoài function => local scope
    - Vòng đời - thời gian tồn tại của biến là khoảng thời gian biến đó thoát khỏi memory.
    Thời gian tồn tại của biến trong function = thời gian thực thi (chạy) function.
    Các biến sẽ bị hủy sau khi return từ function => function không nhớ giá trị biến trong các lần call trước
"""


def my_function():
    age = 30
    print(f"Value of age (inside function) {age}")


age = 18
print(f"Value of age (outside function) {age}")
my_function()
print(f"Value of age (outside function, after call function) {age}")

""" Giải thích:
    - Đầu tiên thấy age được khởi tạo giá trị 18.
    Trong hàm my_function age thay giá trị thành 30, và cái này ko làm ảnh hưởng gì cái bên ngoài cả
    - Bởi vì, age trong hàm là một cái biến khác (local) so với cái bên ngoài.
    Mặc dù nó cùng tên, nhưng là 2 biến khác nhau với phạm vi cũng khác nhau luôn.
    - Các biến khai báo bên ngoài hàm có thể được thấy bên trong hàm => global scope
    Có thể đọc giá trị của nó từ trong hàm, nhưng không thể thay đổi (ghi) chúng.
    Để thay đổi (ghi) giá trị của biến ngoài hàm thì cần khai báo thành biến global bằng từ khóa global
"""


""" Types of function
    - Built-in function: Các hàm cung cấp sẵn trong ngôn ngữ
    Ví dụ: abs(), dict(), set(), input(), ...
    - User-defined function: Các hàm được định nghĩa bởi người dùng chúng
    Ví dụ: my_function(), odd_factorial(), ...
"""

""" Làm ví dụ sau:
    - Xây dựng hàm tính cạnh còn lại trong tam giác khi biết 2 cạnh và góc xen giữa
    - Tính tổng các giá trị trong list các số nguyên bằng hàm sum() - được cung cấp sẵn trong Python
"""


def func_greet(name, msg):
    """
    Đây là hàm greet,
    sẽ in ra câu chào hỏi người có tên được truyền vào.
    """
    print(f"Hello {name}. {msg}")


func_greet('Yuki', 'Good night!')
func_greet('Ame')  # TH1: Thiếu tham số => Lỗi: TypeError: func_greet() missing 1 required positional argument: 'msg'
func_greet()  # TH2: Không tham số => Lỗi: TypeError: func_greet() missing 2 required positional arguments: 'name' and 'msg'
func_greet('Ame', 'Hi', 'I am Yuki!')  # TH3: Thừa tham số: TypeError: func_greet() takes 2 positional arguments but 3 were given


""" Phân tích:
    - Hàm func_greet trên có 2 tham số truyền vào là: name và msg (đây là 1 function có đối số cố định)
    - Khi gọi hàm, truyền đầy đủ 2 tham số thì thấy hàm thực thi bình thường, ko có lỗi gì xảy ra cả.
    - Nếu gọi nó với số lượng tham số khác thì nó sẽ có lỗi (như 3 cách gọi trên)
"""

""" Python cung cấp các cách khác nhau để định nghĩa function với số lượng đối số không cố định """
""" - Cách 1: Tham số với giá trị mặc định.
    Tham số nào có giá trị mặc định thì có thể không cần truyền lúc gọi hàm, khi ko truyền thì nó lấy giá trị mặc định,
    còn nếu truyền thì nó sẽ lấy giá trị truyền vào đó; còn tham số không có giá trị mặc định thì vẫn bắt buộc.
    Được phép dùng bao nhiêu tham số có giá trị mặc định cũng đc. Nhưng khi nó có tham số mang giá trị mặc định,
    thì tất cả các tham số sau nó cũng phải mang giá trị mặc định
"""


def func_greet(name, msg='Good morning!'):
    """
    Đây là hàm greet,
    sẽ in ra câu chào hỏi người có tên được truyền vào.
    """
    print(f"Hello {name}. {msg}")


func_greet('Peter')
func_greet('Paul', 'Hôm nay thế nào?!')

# def func_greet(msg='Good morning!', name):  => Lỗi: SyntaxError: non-default argument follows default argument


""" - Cách 2: Đi kèm tên tham số
    Khi gọi function với một số giá trị, các giá trị có thể được gán theo vị trí của nó.
    Ví dụ: func_greet('Paul', 'Hôm nay thế nào?!') thì 'Paul' được gán cho name, 'Hôm nay thế nào?!' được gán cho msg
    Python cho phép gọi sử dụng tên tham số. Khi dùng cách này, thứ tự các tham số có thể bị thay đổi.
    Có thể dùng cả vị trí và dùng cả tên tham số trong gọi hàm. Nhưng các dùng tên tham số phải sau các dùng vị trí
"""

func_greet(name='Pham Hoan', msg='Morning!')  # Dùng tên với cả 2 tham số
func_greet(msg='Morning!', name='Pham Hoan')  # Dùng tên với cả 2 tham số và thứ tự thay đổi
func_greet('Python', msg='Bạn thế nào?')  # Dùng 1 vị trí và dùng 1 tên tham số

# func_greet(name='Huy NKQ', 'Đang làm gì đó?')  # Lỗi: SyntaxError: non-keyword arg after keyword arg


""" - Cách 3: Số lượng tham số tùy ý
    Python cho phép định nghĩa hàm với số lượng tham số bất kì.
    Khi đó, trong hàm dùng thêm dấu hoa thị (*) trước tham số để biểu thị cho nhiều tham số.
"""


def func_greet(*names):
    for name in names:
        print(f'Hi {name}')


func_greet('C/C++', 'Python', 'Java', 'C#', 'Golang')
""" Đây là cách gọi hàm nhiều tham số, các tham số sẽ được gói lại thành tuple rồi được truyền vào hàm.
    Bên trong, dùng for để duyệt các phần tử từ tuple để lấy tất cả các đối số ra.
"""

""" Anonymous function là gì?
    - Là hàm mà không có tên
    - Hàm thông thường sẽ được định nghĩa với từ khóa def, còn hàm anonymous dùng từ khóa lambda
    - Hàm anonymous (vô danh) có tên khác là hàm lambda
"""
""" Sử dụng hàm lambda như nào?
    - Cú pháp:
        lambda arguments: expression
    - Được phép dùng nhiều tham số (arguments) nhưng chỉ được dùng 1 biểu thức (expression)
    - expression có giá trị và đây chính là giá trị trả về của hàm
    - Được dùng tại bất kì nơi nào mà cần dùng function object
"""

square = lambda x: x * x  # Đây là hàm lambda, x là tham số, x * x là biểu thức
print(square(5))
# Hàm trên không có tên, nó sẽ trả lại một function object và được gán vào biến square, nó gần giống với hàm thường sau

def square(x):
    return x * x


""" Khi nào dùng Lambda function:
    - Khi cần 1 hàm không tên và trong 1 thời gian ngắn
    - Thường dùng làm tham số cho các hàm cấp cao hơn (hàm lấy hàm khác làm tham số đầu vào)
    - Dùng nhiều trong các hàm built-in như filter(), map(), ...
"""
""" Ví dụ dùng với filter()
    - Nhận tham số là một function và 1 list
    - Tham số function sẽ được gọi với tất cả các phần tử của list và một list mới được trả ra chứa các phần tử
    mà tham số function xác định là True
"""
my_list = [1, 2, 5, 8, 9, 6, 7, 0]
# Lấy các phần tử là số chẵn trong list trên
so_chan_list = list(filter(lambda x: x % 2 == 0, my_list))
print(so_chan_list)

""" Ví dụ dùng với map()
    - Nhận tham số là một function và 1 list
    - Tham số function sẽ được gọi với tất cả các phần tử trong list và một list mới được trả ra chứa các phần tử
    mà được trả lại từ tham số function
"""
my_list = [1, 2, 5, 8, 9, 6, 7, 0]
# Tính bình phương các giá trị trong list
square_list = list(map(lambda x: x * x, my_list))
print(square_list)


# Biến Global - toàn cục, Biến Local - cục bộ
""" Global variable
    - Được khai báo bên ngoài hàm hoặc trong phạm vi toàn cục
    - Được truy cập cả bên trong hoặc bên ngoài hàm
"""

x = 'global'


def func():
    print(f"x inside: {x}")


func()
print(f"x outside: {x}")

# trong phạm vi ngoài hàm func tạo biến global x, trong hàm in ra giá trị x. Sau đó gọi hàm func


# x = 'global'
# def func():
#     x = x + x  # Lỗi: UnboundLocalError: local variable 'x' referenced before assignment
#     print(x)
# func()

""" Khi cố tính thay đổi giá trị biến toàn cục trong hàm
    - Sẽ gặp lỗi UnboundLocalError
    - Python hiểu x là biến local và ko thấy khai báo trong hàm
    - Cách khắc phục dùng từ khóa global của python
"""

# Ví dụ dùng từ khóa global
c = 0  # global variable


def add():
    global c  # dùng từ khóa global
    c = c + 2  # increment by 2
    print("Inside add():", c)


add()
print("Outside:", c)


""" Local Variable:
    - Được khai báo trong thân function hoặc trong phạm vi cục bộ
"""


# def func():
#     y = 'local'
#     print(y)
# func()
# print(y)  # Cố tình truy cập biến từ ngoài hàm func => Lỗi: NameError: name 'y' is not defined


# Sử dụng biến global và local trong cùng đoạn code
x = "global"


def func():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


func()
# Định nghĩa biến toàn cục x, và biến cục bộ y trong hàm func. Thay đổi giá trị của x và in cả x và y ra.
# Sau khi gọi hàm func, giá trị x được thay đổi

# Sử dụng các biến global và local cùng tên
x = 'global'


def func():
    x = 'local'
    print(f"Local x: {x}")


func()
print(f"Global {x}")

# Dùng cùng tên x cho biến toàn cụ và cục bộ, nhận thấy sự khác nhau trong kết quả in ra.
# Khi in biến x trong func, nó in đúng giá trị của biến cục bộ => Phạm vị cục bộ của biến
# Tương tự, khi in biến x ngoài func, nó in đúng giá trị của biến toàn cục => Phạm vị toàn cục của biến


""" Recursion Function - Hàm đệ quy
    - Đệ quy là gì? Là quá trình định nghĩa một cái gì đó theo chính nó
    - Đã biết, function có thể gọi đến function khác, và giờ nó thậm chí nó còn có thể gọi đến chính nó => Hàm đệ quy
    - Cách hoạt động - như ảnh python-recursion.jpg
"""

# Ví dụ 1. Viết hàm đệ quy tính giai thừa của số tự nhiên n


def factorial(n):
    """ Đây là hàm đệ quy,
    tính giai thừa của số tự nhiên n
    """
    if n <= 1:  # Đây gọi là điều kiện cơ sở hay điều kiện dừng đệ quy, bắt buộc, nếu ko đệ quy sẽ chạy vô hạn
        return 1
    else:
        return n * factorial(n-1)  # Gọi lại chính nó với giá trị tham số ban đầu trừ 1


number = 5
print(f"{number}! = {factorial(number)}")


""" Cách họat động như sau:
    (1) n = number = 5 => call factorial(5) => chạy đến 5 * factorial(5-1)
    (2) => call factorial(4) => chạy đến 4 * factorial(4-1)
    (3) => call factorial(3) => chạy đến 3 * factorial(3-1)
    (4) => call factorial(2) => chạy đến 2 * factorial(2-1)
    (5) => call factorial(1) => trả lại 1
    (6) => quay lại (4), factorial(2) = 2 * 1
    (7) => quay lại (3), factorial(3) = 3 * 2 * 1
    (8) => quay lại (2), factorial(4) = 4 * 3 * 2 * 1
    (9) => quay lại (1), factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
"""
""" Nhận thấy, đệ quy với quy nạp toán học có điểm tương đồng
    Khi làm thì cần định nghĩa được bài toán qua chính nó => chính là tìm công thức truy hồi
"""
# Ví dụ: Viết hàm đệ quy để tính số Fibonacci thứ n, biết F(1) = F(2) = 1, F(n) = F(n-1) + F(n-2)


def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input("Nhập n = "))
print(f"Số Fibonacci thứ {n} là {fibo(n)}")

"""
Ưu điểm của đệ quy
    - Nhìn gọn gàng và trong sáng
    - Một task phức tạp có thể được chia thành các bài toán con khi dùng đệ quy
    - Tạo ra sequence bằng đệ quy dễ hơn dùng lặp lồng nhau
Nhược điểm của đệ quy:
    - Đôi khi logic ẩn trong đệ quy khá khó
    - Gọi đệ quy thường không hiệu quả vì dùng nhiều memory và time
    - Hàm đệ quy khó debug
"""