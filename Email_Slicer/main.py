"""
if __name__ == __main__ là gì?

-> Việc sử dụng condition này sẽ giúp cho các "Sub_module" hạn chế chạy song hành với "main_module".

if __name == "__main__":
  sub_main()

=> hàm "sub_main()" chỉ được chạy khi mà chúng ta chạy file "sub_module" là file chính

"""

"""
Đây là 1 Pet Project nhỏ giúp chúng ta có thể cắt được Username của Email và Email Domain của Email

VD: anhratdeptrai@gmail.com
- Username : anhratdeptrai
- Email Domain : gmail.com

"""

from sub_module import emailProcess, printMsg

def main():
  emails = ['s1@gmail.com', 's12@gmail.com', 's123@gmail.com', 's34@gmail.dev', 's45@edu.com.vn']
  for email in emails:
    username, email_domain = emailProcess(email)
    printMsg(username, email_domain)


if __name__ == "__main__":
  main()