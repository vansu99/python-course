""" Exception:
    - Handling
    - Except clause
    - try-finally clause
"""

""" Python errors và Built-in Exceptions
    - Syntax/Parsing errors: Lỗi do không tuân theo cú pháp của ngôn ngữ
    - Logical errors (Exceptions): Lỗi xảy ra trong thời gian chạy (sau khi qua kiểm tra cú pháp)
    Ví dụ:
        - Cố tình mở 1 file chưa có lên để đọc - FileNotFoundError
        - Cố tình chia cho 0 - ZeroDivisionError
        - Có tình import module không tồn tại - ImportError
        - Có tình ép kiểu không đúng - ValueError
"""
# Chạy thử các ví dụ sau
print(1/0)  # Chi cho 0
a = int('9.a')  # Ép kiểu với giá trị ko đúng định dạng số nguyên
open('file_not_found.txt')  # file không tồn tại

""" Danh sách các exception phổ biến mà python dựng sẵn ảnh common_built-in_exceptions.PNG """

""" Khi các exception xảy ra, nó sẽ làm cho chương trình bị dừng lại và chuyển lên nơi mà gọi nó,
nếu không handled thì sẽ bị crash.
    Ví dụ: A gọi B và B gọi tiếp sang C; nếu trong C có exception mà không được handled thì nó sẽ đẩy lên B và tiếp tục lên A.
    Và cuối cùng ko được handled thì có một thông báo error hiện lên, chương trình sẽ dừng đột ngột.
    => Để bắt và xử lý được các exception thì chúng ta sẽ dùng các lệnh try, except và finally.
"""

""" Bắt exception, với ví dụ sau - chưa chỉ rõ exception cụ thể """
import sys

random_list = ['a', 0, 0.5]

for item in random_list:
    try:
        print("Phần tử:", item)
        r = 1 / int(item)
        print("Nghịch đảo của ", item, "is", r)
    except:
        print("Oops!", sys.exc_info()[0], "Toang Rồi!.")  # import module sys to get the type of exception
        print("=> next \n")

""" Bắt exception, với ví dụ sau - chỉ rõ exception cụ thể """

try:
    # Code gì đó có thể gây exception
    pass

except ValueError:
    # Xử lý nếu như exception loại ValueError xảy ra
    pass

except (TypeError, ZeroDivisionError):
    # Xử lý nếu như gặp nhiều exceptions cùng lúc, ở đây đang xét 2 loại TypeError và ZeroDivisionError
    pass

except:
    # Xử lý tất cả các loại exceptions khác 3 loại trên
    pass

""" Raising Exceptions, xét các ví dụ sau để xem về việc raise exception """

raise KeyboardInterrupt

raise MemoryError("This is an argument")

try:
    a = int(input("Nhập một số nguyên dương: "))
    if a <= 0:
        raise ValueError("Số vừa nhập không phải số nguyên dương!")
except ValueError as ve:
    print(ve)

""" Dùng câu lệnh: try-finally
    - Câu lệnh try đi kèm với câu lệnh finally thì các câu lệnh trong khối finally sẽ luôn được thực thi dù có chuyện gì đi nữa!
    - Các câu lệnh trong finally thường dùng để giải phóng tài nguyên cho phần đang chạy
"""
# Nhớ lại về phần file đã có đoạn try-finally như sau:
try:
    f = open("test.txt", encoding='utf-8')
    # Làm gì đó với file trên nếu như mở thành công
finally:
    f.close()
# Luôn đảm bảo tệp được đóng ngay cả khi có ngoại lệ xảy ra.