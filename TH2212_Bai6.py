n = int(input('Nhap vao so luong bai hat :'))
ds_bai_hat =[]
for i in range(n):
    ten_bai_hat = input(f'Ten bai hat thu {i+1} la :') 
    ds_bai_hat.append(ten_bai_hat)

for i in range(n):
    ten = ds_bai_hat[i]
    print(f'Bai {i+1} la : {ten} ')


for bai in ds_bai_hat:
    
    print(bai.upper())





