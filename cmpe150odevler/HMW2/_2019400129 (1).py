
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
my_list=[]
number=0
row = x+g
column=0
while(number<=g+x):
    list1=[]
    if(number<x):
        for b in range(y):
            list1.append("*")
    elif(x<=number and number<g+x):
        for a in range(y):
            list1.append(" ")
    elif(number==g+x):
        for c in range(y):
            list1.append(" ")
        if(y%2!=0):

            list1[y//2]="@"
            column=y//2
        else:
            list1[y//2-1]="@"
            column = y // 2-1
    my_list.append(list1)
    number+=1

score=0
time=0
gameFinished=False
clear=True
while(score<x*y and gameFinished== False):
    if(time%5==0 and time!=0):

        for r in range(y):
            if(my_list[row-1][r] == "*"):
                clear=False

        if(clear==True):
            list2=[]
            for h in range(y):
                list2.append(" ")
            my_list.insert(0,list2)
            my_list.pop()
            my_list[row][column]="@"

        else:
            gameFinished=True

        if(gameFinished==True):
            print("GAME OVER")
            for a in range(x + g + 1):
                for b in range(y):
                    print(my_list[a][b], end="")

                print()
            print("------------------------------------------------------------------------")

            print("YOUR SCORE: "+str(score))

            break


    for a in range(x + g + 1):
        for b in range(y):
            print(my_list[a][b], end="")

        print()
    print("------------------------------------------------------------------------")


    usr_input=input("Choose your action!")
    print()

    usr_input=usr_input.lower()
    if(usr_input=="exit"):
        for a in range(x + g + 1):
            for b in range(y):
                print(my_list[a][b], end="")

            print()
        print("------------------------------------------------------------------------")
        print("YOUR SCORE: "+str(score))
        break

    elif(usr_input == "right" and column<y-1):
        my_list[row][column]=" "
        my_list[row][column+1] = "@"
        column=column+1


    elif (usr_input == "left" and column>0):
        my_list[row][column] = " "
        my_list[row][column - 1] = "@"
        column = column - 1


    elif (usr_input == "fire"):
        riffle_col=column
        riffle_row=row-1
        my_nbr=-2
        for m in range(row-1,-1,-1):
            if(my_list[m][riffle_col]=="*"):
                my_nbr=m
                break
        if(my_nbr!=-2):
            while (riffle_row > m):
                if (my_list[riffle_row + 1][riffle_col] != "@"):
                    my_list[riffle_row + 1][riffle_col] = " "
                my_list[riffle_row][riffle_col] = "|"
                for a in range(x + g + 1):
                    for b in range(y):
                        print(my_list[a][b], end="")

                    print()
                print("------------------------------------------------------------------------")

                riffle_row -= 1
            my_list[riffle_row + 1][riffle_col] = " "
            my_list[riffle_row][riffle_col] = " "
            my_list[row][column] = "@"
            score+=1

        else:
            while (riffle_row > -1):
                if (my_list[riffle_row + 1][riffle_col] != "@"):
                    my_list[riffle_row + 1][riffle_col] = " "
                my_list[riffle_row][riffle_col] = "|"
                for a in range(x + g + 1):
                    for b in range(y):
                        print(my_list[a][b], end="")

                    print()
                print("------------------------------------------------------------------------")

                riffle_row -= 1
            my_list[riffle_row + 1][riffle_col] = " "
            my_list[riffle_row][riffle_col] = " "
            my_list[row][column]="@"

    time=time+1

if(score==x*y):
    print("YOU WON!")
    for a in range(x + g + 1):
        for b in range(y):
            print(my_list[a][b], end="")

        print()
    print("------------------------------------------------------------------------")
    print("YOUR SCORE: "+str(score))



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
