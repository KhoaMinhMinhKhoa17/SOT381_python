n = int(input('Nhập vào số n : '))
S3 = 0
for i in range(1, n +1) :
    S3 += 1 / (i * (i + 1 ))
print('Vậy S3 = ', S3)