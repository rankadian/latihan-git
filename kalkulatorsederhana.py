# proses input user
print('=' * 30)
print('   Kalkulator Sederhana')
print('   Operasi Matematika')
print('=' * 30)
print(' 1. Penjumlahan    (+)')
print(' 2. Pengurangan    (-)')
print(' 3. Perkalian      (*)')
print(' 4. Pembagian      (/)')
print('=' * 30)

operasi = input('Pilih Operasi (1/2/3/4): ')
bil1 = eval(input('Masukan Bilangan Pertama : '))
bil2 = eval(input('Masukan Bilangan Kedua : '))
print('=' * 30)

#proses percabangan dasar
if operasi == '1':
    print('User Memilih Operasi Penjumlahan')
elif operasi == '2':
    print('User Memilih Operasi Pengurangan')
elif operasi == '3':
    print('User Memilih Operasi Perkalian')
elif operasi == '4':
    print('User Memilih Operasi Pembagian')
else:
    print('Tidak Valid!!!!!!!!!!')
    
# proses perhitungan dan menampilkan hasil operasi
if operasi == '1':
    hasil = bil1 + bil2
    print(f'Hasil Operasi Dari {bil1} + {bil2} = {hasil}')
elif operasi == '2':
    hasil = bil1 - bil2
    print(f'Hasil Operasi Dari {bil1} - {bil2} = {hasil}')
elif operasi == '3':
    hasil = bil1 * bil2
    print(f'Hasil Operasi Dari {bil1} * {bil2} = {hasil}')
elif operasi == '4':
    hasil = bil1 / bil2
    print(f'Hasil Operasi Dari {bil1} / {bil2} = {hasil}')
else:
    print('Tidak Valid!!!!!!!!!!')
print('=' * 30)
    