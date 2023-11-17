def hitung_gaji_kotor(gaji_pokok, tunjangan):
    # Kesalahan dalam perhitungan gaji kotor (software fault)
    return gaji_pokok - tunjangan  # Seharusnya tambah, bukan kurang

def main():
    print("Gaji Kotor Anda :",hitung_gaji_kotor(5000,1000)) # Expected result = 6000

if __name__ == '__main__':
    main()