def printit(x): #prints a matrix (a nested list)
    for ele in x:print ' '.join(map(str,ele))
def transpose(x): #returns the transpose of a matrix
    return map(list,zip(*x))


n=input()
L=[[0 for i in range(n)]for j in range(n)]
counter=1
i,j=0,n/2
while counter<=n**2:
    L[i][j]=counter
    counter+=1
    newi,newj=(i-1)%n,(j+1)%n  #this is really clever, however I do not take credit for this xD This is done by some other humble soul 
    if L[newi][newj]!=0:
        i+=1  #no up-right movement needed, according to alg just move down
    else:
        i,j=newi,newj #up-right movement done only when there is a free space at required position

#L is currently a magic square. the code below is executed so as to fit the expected output.
L=(transpose(L))
new=[]
for ele in L:
    new.append(ele[::-1])
L=new[::-1]

printit(L)

##For testing purposes, and confirming result:-
#def ismagic(x,magicsum):
#    rowsum,colsum,l=[],[],len(x[0])
#    for i in x:rowsum.append(sum(i)==magicsum)
#    for i in transpose(x):colsum.append(sum(i)==magicsum)
#    d1= [x[i][i] for i in range(l)]             
#    d2= [x[l-1-i][i] for i in range(l-1,-1,-1)]
#    diagsum=(sum(d1),sum(d2))==(magicsum,magicsum)
#    if all(rowsum) and all(colsum) and diagsum:
#        return True
#    return False
#magicsum=(n*(n**2+1))/2
#print ismagic(L,magicsum)