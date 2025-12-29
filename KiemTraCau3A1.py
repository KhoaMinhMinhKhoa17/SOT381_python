n = int(input('Nhập vào số n : '))
so = []

for i in range(n) :
    k = int(input(f'Nhập phần tử thứ {i+1}  '))
    so.append(k)
bo_dem = 0
for k in so :
    if k % 2 == 0 :
        bo_dem += 1
print('Số lượng các phần tử có  giá trị chẵn là : ', bo_dem)