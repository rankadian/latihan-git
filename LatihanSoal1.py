#soal 1
print("=" * 40)
print("Program Menampilkan Bilangan Kelipatan 3")
print("=" * 40)\
    
nilai = int(input("Masukan Bilangan : "))
    
for i in range(1, nilai+1):
    print(i*3,end="")
        
print()
        
#soal 2
print("=" * 30)
print("     Program Segitiga Angka      ")
print("=" * 30)

tinggiSegitiga = int(input("Masukan Tinggi Segitiga : "))
print()

for i in range(1,tinggiSegitiga):
    for j in range(1,i+1):
        print(j,'',end='',sep='')
    print()
    
#soal 3
print("=" * 50)
print("Program Menghitung dan Menampilkan Nilai Mahasiswa")
print("=" * 50)

nama        = input("Masukan Nama Anda : ")
tugas       = int(input("Masukan Nilai Tugas Anda          : "))
quiz        = int(input("Masukan Nilai Kuis Anda           : "))
uts         = int(input("Masukan Nilai Tugas UTS           : "))
uas         = int(input("Masukan Nilai Tugas UAS           : "))
nilai_akhir = int(input("Masukan Nilai Nilai Akhir Anda    : "))

print()
print("=" * 21)
print("Hasil Nilai Mahasiswa")
print("=" * 21)
print()

print("Nama Mahasiswa       : ")
print("Nilai Tugas          : ")
print("Nilai Kuis           : ")
print("Nilai UTS            : ")
print("Nilai UAS            : ")
print("Nilai Nilai Akhir    : ")
print()
nilai = tugas + quiz + uts + uas + nilai_akhir
print("Jumlah Nilai Anda Semua : ", nilai)
if nilai >= 450:
    print("Selamat Anda Mendapat Nilai Grade A")
elif nilai >= 400:
    print("Selamat Anda Mendapat Nilai Grade B")
elif nilai >= 350:
    print("Selamat Anda Mendapat Nilai Grade C")
elif nilai >= 300:
    print("Selamat Anda Mendapat Nilai Grade D")
else:
    print("Anda Harus Lebih Giat Belajar Lagi")
#selesai