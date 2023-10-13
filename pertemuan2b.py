#Fungsi Cek(a,b)
#parameter a,b : integer
#fungsi kirimkan nilai hasil
def Cek(a,b):
    if (a > 10 and b > 0):
        hasil = 1
    else:
        hasil = 0
    return hasil

def main():
    # test case-1
    a=50; b=5
    print("Hasil :",Cek(a,b))
    #expected result = 1
    return 0

if __name__ == '__main__':
    main()