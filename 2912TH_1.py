toan = float(input('Nhap vao diem toan cua hoc sinh '))
ly = float(input('Nhap vao diem ly cua hoc sinh '))
hoa = float(input('Nhap vao diem hoa cua hoc sinh '))
tong = 0 
tong = toan + ly + hoa
if tong >= 15 and toan >=4 and ly >=4 and hoa >=4 :
    print('Dau')
    if toan > 5 and ly > 5 and hoa > 5:
        print('Hoc deu cac mon')
    else :
        print('Hoc chua deu ')
else :
    print('Chua tay dau ')