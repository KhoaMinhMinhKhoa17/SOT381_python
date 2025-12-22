def sln(a,b,c):
    return max(a,b,c)
def snn(a,b,c):
    return min(a,b,c)
a = int(input('Nhap vao so a : '))
b = int(input('Nhap so b : '))
c = int(input('Nhap so c : '))

print('So lon nhat la ', sln(a,b,c))
print('So be nhat la ', snn(a,b,c))