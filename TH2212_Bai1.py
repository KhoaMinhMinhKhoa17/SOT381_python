while True:
 w = float(input('Nhap vao chieu dai cua hcn : '))
 h = float(input('Nhap vao chieu rong cua hcn : '))
 if 0.0<=w and h<=100.0 :
    break
else:
    print('Sai roi')
P = (w + h)*2
S = w *h
print(f'Chu vi hcn la  {P}')
print(f'Dien tich hcn la {S}')

    
