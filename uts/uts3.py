# Fungsi Asli
def tambah(a, b):
    return a + b

# Mutant 1: Mengganti operator penjumlahan dengan pengurangan
def mutant_1(a, b):
    return a - b

# Mutant 2: Mengganti operator penjumlahan dengan perkalian
def mutant_2(a, b):
    return a * b

# Mutant 3: Menambah operan tetapi tetap menggunakan operator penjumlahan
def mutant_3(a, b, c):
    return a + b + c

# Test Case 1 (a=10; b=1)
test_case_1_original = tambah(10, 1)
test_case_1_mutant_1 = mutant_1(10, 1)
test_case_1_mutant_2 = mutant_2(10, 1)
test_case_1_mutant_3 = mutant_3(10, 1, 0)

# Test Case 2 (a=11; b=0)
test_case_2_original = tambah(11, 0)
test_case_2_mutant_1 = mutant_1(11, 0)
test_case_2_mutant_2 = mutant_2(11, 0)
test_case_2_mutant_3 = mutant_3(11, 0, 0)

# Test Case 3 (a=12; b=2)
test_case_3_original = tambah(12, 2)
test_case_3_mutant_1 = mutant_1(12, 2)
test_case_3_mutant_2 = mutant_2(12, 2)
test_case_3_mutant_3 = mutant_3(12, 2, 1)

# Analisis Tabel
print("Test Case\tFungsi Asli\tMutant 1\tMutant 2\tMutant 3")
print(f"1\t\t{test_case_1_original}\t\t{test_case_1_mutant_1}\t\t{test_case_1_mutant_2}\t\t{test_case_1_mutant_3}")
print(f"2\t\t{test_case_2_original}\t\t{test_case_2_mutant_1}\t\t{test_case_2_mutant_2}\t\t{test_case_2_mutant_3}")
print(f"3\t\t{test_case_3_original}\t\t{test_case_3_mutant_1}\t\t{test_case_3_mutant_2}\t\t{test_case_3_mutant_3}")
