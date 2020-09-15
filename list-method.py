# -------------------- Bài 13 -----------------------

a = [1, 2, 3, 4, 5, 5]
b = a.count(5) # số lần xuất hiện trong list
print('b: ', b) # 2


c = a.index(1) # vị trí đầu tiên nằm trong list
print('c: ', c) # 0


d = a.copy() # tạo ra 1 bản sao nhưng không trở về 1 vùng nhớ
print('d: ', d) # [1, 2, 3, 4, 5, 5]


e = a.clear() # xóa tất cả item ra khỏi list nên không cần một tham số truyền vào
print('e: ', e) # None


f = [1, 2, 3, 4]
g = f.append([5, 6]) # thêm phần tử truyền vào vào mảng f
print('g: ', f) # [1, 2, 3, 4, [5, 6]]


h = [1, 2, 3, 4]
i = h.extend([5, 6, [7, 8]]) # lấy ra từng phần tử và nhét vào bên trong h
print('h: ', h) # [1, 2, 3, 4, 5, 6. [7, 8]]


k = [1, 2, 3, 4]
l = k.insert(2,5) # thêm vào phần tử 5 vào vị trí index = 2 vào trong mảng k, nếu index truyền vào không có trong mảng nó sẽ đưa về cuối mảng, nếu index âm sẽ truyền từ dưới lên
print('k: ', k) # [1, 2, 5, 3, 4]


m = [1, 2, 3, 4]
n = m.pop(1) # bỏ đi phần tử thứ i trong mảng
print('m: ', m) # [1, 3, 4]
print('n: ', n) # 2


o = [1, 1, 1, 2, 3, 4]
p = o.remove(1) # bỏ đi phần tử đầu tiên trong list
print('o: ', o) # [1, 1, 2, 3, 4]


q = [1, 2, 3, 4]
r = q.reverse() # đảo ngược vị trí trong list
print('q: ', q) # [4, 3, 2, 1]


s = [3, 1, 4, 6, 2]
t = s.sort() # sắp xếp thứ tự trong mảng nếu là số
# s.sort(key=None, reverse=False) mặc định, nếu đảo ngược lại có thể dùng s.sort(reverse=True)
print('s: ', s) # [1, 2, 3, 4, 6]


