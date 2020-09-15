#trong kiểu dữ liệu float sau dấu . chỉ lấy tối đa 15 chữ số.

#láy toàn bộ thư viện decimal
# từ thư viện decimal, import mọi thứ vào
from decimal import*

#lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 30;

a = 10/3
print(a);
print(type(a))

b = Decimal(10)/Decimal(3)
print(b)
print(type(b))

#Fraction: Phân số
from fractions import*

frac1 = Fraction(6,9);
frac2 = Fraction(1,9);

frac = frac1 + frac2

print(frac)
print(type(frac))


#complex: số phúc, j^2 = -1
c = complex(2, 5)
#lấy phần thực
print(c.real)
#lấy phần ảo
print(c.imag)
print(c)
print(type(c))


#lấy phần nguyên
d = 10//3
print(d)

#lấy phần dư
e = 10%3
print(e)

#luỹ thừa

f = 2**2
print(f)


# thư viện math
import math

#lấy phần nguyên
print(math.trunc(3.9))

#làm tròm xuống
print(math.floor(3.3))

#làm tròn lên
print(math.ceil(3.3))

#căn bậc 2
print(math.sqrt(16))

#trị tuyệt đốt
print(math.fabs(-16))

#trả về 1 số nguyên là UCLN của x và y
print(math.gcd(6, 4))