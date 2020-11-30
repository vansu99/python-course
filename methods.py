# Cách sử dụng map, filter, generator trong Python

"""
Map
  - map(function_name, list_name)

"""

def getPrice(price, tax = 1.08):
  return int(price * tax)

lists_price = [10, 20, 30, 40]

result = list(map(getPrice, lists_price)) # ouput: [10, 21, 32, 43]

# Dùng Map với Lambda
result2 = list(map(lambda price, tax = 1.08: int(price * tax), lists_price))

"""
Filter

  - sẽ truyền vào 2 tham số: list_name và condition
  - trả về 1 list mới chứa các phần tử đã được lọc (thỏa mãn) điều kiện mà mình truyền vào

"""

result3 = [price for price in lists_price if price >= 20]
print(result3)

"""
Generator

  - 1 hàm không có return
  - dùng syntax "yield"
  - mỗi lần gọi hàm "next()" sẽ trả về 1 giá trị tương ứng cho đến khi không còn giá trị

"""
teams = {"Zmem": "Ateam", "Hmem"L "Ateam", "Kmem": "Bteam", "Tmem": "Cteam"}
print(teams)
# Sắp xếp lại Dict
for item in sorted(teams.items, key=lambda i: i[0])

my_list = [0,1,2,3,4,5]

# comprehension
my_comp = [l for l in my_list if l % 2 == 0]
print(my_comp)

# Generator
my_gen = (l for l in my_list if l % 2 == 0)
print(my_gen) # không ra giá trị cần tìm

# muốn in ra giá trị cần tìm thì gọi "next(generator_name)"

next(my_gen) # output: 0 (lần 1)
next(my_gen) # output: 2 (lần 2)
next(my_gen) # output: 4 (lần 3)
next(my_gen) # output: báo lỗi -> vì không còn value để trả về (lần 4)

weekdays = ["mon", 'tue', 'wen', 'thur', 'fri', 'sat', 'sun']

def getDay():
  for day in weekdays:
    yield day

w = getDay()
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print('---------')
print(next(w))
print(next(w))


