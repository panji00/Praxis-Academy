standar deviasi
def SD(data):
    jumlah = 0
    for i in range (len(data)):
        jumlah + data[i]

    rata = jumlah/len(data)
    sigma = 0
    for i in range (len(data)):
        hitung = (data[i] - rata)**2
        sigma += hitung
    pembagian=sigma/len(data)
    standarDeviasi=pembagian **0.5
    print("nilai standar deviasi adalah: ", standarDeviasi)
data =([5, 6, 3, 9, 3, 6, 7, 8])
SD(data)

def baku(data):
    bk = (data - 21.25) / 6.214901447328026

data=numpy.array([5, 6, 3, 9, 3, 6, 7, 8])
baku(data)

#rata-rata
def RB(data):
    jumlah=0
    for i in range (len(data)):
        jumlah +=data[i]
        rata=jumlah/len(data)
    print("Jumlah Data: ", len(data))
    print("Total Nilainya: ", jumlah)
    print("Nilai rata-ratanya adalah: ", rata)
data = ([5, 6, 3, 9, 3, 6, 7, 8])
RA(data)



def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y
  
def kali(x, y):
    return x * y
  
def bagi(x, y):
    return x / y
 
print("pilih aritmatika -\n" \
        "1. tambah\n" \
        "2. kurang\n" \
        "3. kali\n" \
        "4. bagi\n")
  
#pilih menu operasi
while True:
    pilih = int(input("silahkan pilih 1, 2, 3, 4 :"))
    
    number_1 = int(input("Masukan bilangan pertama: "))
    number_2 = int(input("Masukan bilangan kedua: "))
    
    if pilih == 1:
        print(number_1, "+", number_2, "=",
                        tambah(number_1, number_2))
    
    elif pilih == 2:
        print(number_1, "-", number_2, "=",
                        kurang(number_1, number_2))
    
    elif pilih == 3:
        print(number_1, "*", number_2, "=",
                        kali(number_1, number_2))
    
    elif pilih == 4:
        print(number_1, "/", number_2, "=",
                        bagi(number_1, number_2))
    else:
        print("Invalid input")
    #kembali ke awal

    kembali=input('ingin kembali kepilihan awal? (y/t) : ')
    if kembali=='y':
        continue
    elif kembali=='t':
        break
    else:
        break
