import math
a = float(input('Nhap vao canh dau tien cua tam giac : '))
b = float(input('Nhap vao canh thu hai cua tam giac : '))
c = float(input('Nhap vao canh thu ba cua tam giac : '))
P = a + b + c 
p = P / 2
S = math.sqrt(p*(p - a)*(p - b)*(p - c))
print(f'Dien tich tam giac la {S} ')