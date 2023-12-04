#Fungsi lastMin(x)
#parameter x : array of integer
#fungsi mencari nilai terkecil terakhir dalam array x
#min : posisi nilai terkecil terakhir dalam array
def lastMin(x):
    min = 0
    for i in range (1,len(x),1):
        if (x[i]<= x[min]):
            print(x[i]<= x[min])
            min = i
    return min

def main():
    #test case array A
    A = [9,5,7,5]
    print("last min in A :",lastMin(A)) #expected result = 3


    return 0

if __name__ == '__main__':
    main()