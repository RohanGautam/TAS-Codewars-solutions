#declaring some functions that will be used in the program and while debugging:-
def isfull(x):  #checks if matrix is full
    for i in x:
        if not all(i):return False
    return True
def printit(x): #prints a matrix (a nested list)
    for ele in x:print ' '.join(map(str,ele))

#the main function:-
def fillup(L,n):
    elements=range(1,n**2+1)
    col_upperbound,row_upperbound=n,n
    col_lowerbound,row_lowerbound=0,0
    while isfull(L)==False: #if matrix is not full, execute the commands below
        for i in range(col_upperbound-1,col_lowerbound-1,-1): #moving left from bottom
            L[row_upperbound-1][i]=elements.pop()        
        for i in range(row_upperbound-2,row_lowerbound-1,-1): #moving top on the left side
            L[i][col_lowerbound]=elements.pop()        
        for i in range(col_lowerbound+1,col_upperbound):  #moving right from top
            L[row_lowerbound][i]=elements.pop()        
        for i in range(row_lowerbound+1,row_upperbound-1):#moving down from the right side
            L[i][col_upperbound-1]=elements.pop()
        col_upperbound-=1   #decrementing upperbounds by 1 and incrementing lowerbounds by 1..
        row_upperbound-=1   #..this is done so that the inner unfilled matrix can be accessed
        col_lowerbound+=1
        row_lowerbound+=1
    return L


n=input()
L=[[0 for i in range(n)]for j in range(n)]
L=fillup(L,n)
#to handle the case of n bieng even;
new=[]
if n%2==0:
    for ele in L:
        new.append(ele[::-1])
    L=new[::-1]
#displaying the result.
printit(L)