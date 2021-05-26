import math
print("MENGHITUNG LUAS & KELILING, LINGKARAN & PERSEGI PANJANG")
print('1. Luas lingkarang')
print('2. Keliling lingkarang')
print('3. Luas persegi panjang')
print('4. keliling persegi panjang')


pilihan = input("silahkan pilih(1/2/3): ")

if pilihan == '1':
    r = float(input("Masukan Jari-jari : "))
    luas = math.pi*(r*r)
    print ("Luas Lingkaran \t\t= ",luas)

elif pilihan == '2':
    r = float(input("Masukan Jari-jari : "))
    keliling = 2*math.pi*r
    print ("Keliling Lingkaran\t= ",keliling)

elif pilihan == '3':
    panjang = float(input("\nMasukan Panjang: "))
    lebar = float(input("Masukan Lebar: "))
    luas = panjang*lebar
    print("\nLuas Persegi Panjang \t\t:",luas)

elif pilihan == '4':
    panjang = float(input("\nMasukan Panjang: "))
    lebar = float(input("Masukan Lebar: "))
    keliling = 2 * (panjang+lebar)
    print("Keliling Persegi Panjang\t:",keliling)