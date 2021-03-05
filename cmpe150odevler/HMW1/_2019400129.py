def hw3():
    cumulative_sum = 0
    n = int(input())
    x = int(input())
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    my_str=""
    for p in range(0,x):
        if(p==0):
            my_str+=input("Pls enter the numbers: ")
        else:
            my_str += input()

    if(n<=x):
        a=0
        k = n
        for m in range(x-1,x-n-1,-1):

            cumulative_sum=cumulative_sum+int(my_str[m])*(10**a)*k
            a=a+1
            k=k-1
    else:
        if(x!=0):
            if(n%x!=0):
                my_str=my_str*((n//x)+1)
            else:
                my_str= my_str * (n // x)

            a = 0
            k = n
            for m in range(x - 1, x - n - 1, -1):
                cumulative_sum = cumulative_sum + int(my_str[m]) * (10 ** a) * k
                a = a + 1
                k = k - 1
        else:
            cumulative_sum=0
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    print(cumulative_sum)
    return cumulative_sum


if __name__ == "__main__":
    hw3()

