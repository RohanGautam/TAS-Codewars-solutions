n=input()
x=n/2 
for i in range(1,x):
    print '#'*(x-i)+'/'*i+u'\\'*i+'#'*(x-i)
print '/'*x+u'\\'*x
print u'\\'*x+'/'*x
for i in range(1,x):
    print '#'*(i)+u'\\'*(x-i)+'/'*(x-i)+'#'*(i)
