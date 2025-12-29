n = int(input('Nhập vào số phần tử của dãy số : '))
list = []
for i in range(n):
    l = int(input(f'Nhập vào phần tử thứ {i+1} : '))
    list.append(l)

tong = 0
for i in range(1,n,2) :
    tong = tong  + list[i]
print('Tổng các số ở vị trí chẵn là : ', tong)