# Program menyapa pengunjung D&Z Cafe
nama = str(input('Masukkan nama pengunjung: \n'))
sex = str(input('Masukkan jenis kelamin  pengunjung (L/P): \n'))

if sex == 'L' or sex == 'l':
    print('"Selamat datang, Tuan', nama, '"')
elif sex == 'P' or sex == 'p':
    print('"Selamat datang, Nyonya', nama, '"')
else:
    print('Kode jenis kelamin salah!')
print()