n = int(input('Nhao vao so n : '))
def tinhS(n):
    ts = 0
    ms = 0

    for i in range(1,n+1) :
        ts += i
        if i % 2 == 0 :
            ms += i 
    S = ts / ms 
    return S

kq = tinhS(n)
print(f'Ket qua S = {kq}')
 


   
    
