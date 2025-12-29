dtb = float(input('Nhap diem trung binh cua hs : '))
if dtb < 0 and dtb > 10 :
    print('ĐIỂM KHÔNG HỢP LỆ')
if dtb >= 6.5 and dtb <= 8.5 :
    print('Khá ')
if dtb >= 5.0 and dtb < 6.5 :
    print('Trung bình ')
if dtb >= 3.5 and dtb < 5.0 :
    print('Kém ')