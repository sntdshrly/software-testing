#Fungsi CountPos(x)
#parameter x : array of integer
#fungsi menghitung banyaknya nilai positif dalam array x
#fungsi kirimkan banyaknya nilai positif
def CountPos(x):
    count = 0
    for i in range (0,len(x),1):
        if (x[i]>=0):
            count = count + 1
    return count

def main():
    #test case array A
    A = [-3,-2,1,0,4]
    print("Bilangan positif dlm A :",CountPos(A))
    # expected result = 2
    return 0

if __name__ == '__main__':
    main()
