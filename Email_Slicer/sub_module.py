def emailProcess(email):
  email_username = email[0:email.index("@")] # Lấy Username của email
  email_domain = email[email.index("@") + 1:] # Lấy Email Domain
  return [email_username, email_domain]

def printMsg(email_username, email_domain):
  print(f"Email Username: {email_username} \nEmail Domain: {email_domain}")

def main():
  email = input("Hãy nhập địa chỉ Email của bạn: ").strip()
  email_username, email_domain = emailProcess(email)
  printMsg(email_username, email_domain)

# Nếu mà file "sub_module" này chạy chính thì hàm main() sẽ được execute
if __name__ == "__main__":
  main()