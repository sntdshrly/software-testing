#Fungsi Cek(a,b)
#parameter a,b : integer
#fungsi kirimkan nilai hasil
def Cek(a,b):
    if (a > 10 and b > 0):
        hasil = 1
    else:
        hasil = 0
    return hasil

def CekMutant1(a,b):
    if (a >= 10 and b > 0):
        hasil = 1
    else:
        hasil = 0
    return hasil

def CekMutant2(a,b):
    if (a > 10 and b >= 0):
        hasil = 1
    else:
        hasil = 0
    return hasil

def CekMutant3(a,b):
    if (a > 10 and b > 0):
        hasil = 2
    else:
        hasil = 0
    return hasil

def main():
    # test case contoh
    a=50; b=5
    # test case-1
    a1=10; b1=1
    # test case-2
    a2=11; b2=0
    # test case-3
    a3=12; b3=2
    
    print("Hasil :",CekMutant1(a1,b1))
    print("Hasil :",CekMutant2(a1,b1))
    print("Hasil :",CekMutant3(a1,b1))

    return 0

if __name__ == '__main__':
    main()