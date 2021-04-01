# Program grading nilai mahasiswa
nama = str(input('Masukkan nama Mahasiswa: \n'))
nilai = float(input('Masukkan nilai Mahasiswa: \n'))

if nilai >= 85:
    print ('"Halo,', nama, '! Nilai anda setelah dikonversi adalah A"')
elif nilai >= 80:
    print ('"Halo,', nama, '! Nilai anda setelah dikonversi adalah A-"')
elif nilai >= 75:
    print ('"Halo,', nama, '! Nilai anda setelah dikonversi adalah B+"')
elif nilai >= 70:
    print ('"Halo,', nama, '! Nilai anda setelah dikonversi adalah B"')
elif nilai >= 65:
    print ('"Halo,', nama, '! Nilai anda setelah dikonversi adalah C+"')
elif nilai >= 60:
    print ('"Halo,', nama, '! Nilai anda setelah dikonversi adalah C"')
elif nilai >= 0:
    print ('"Halo,', nama, '! Nilai anda setelah dikonversi adalah E"')
else:
    print ('Nilai tidak valid!')

print()