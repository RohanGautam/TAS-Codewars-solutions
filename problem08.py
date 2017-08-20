#flow	code	wolf	wars	tas	listen	fast	silent	.	Sample	Output	1	flow	wolf	listen	silent		
#Sample	Input	2	paternal	firetruck	racecar	parental	.		
##Sample	Output	2	paternal	parental		
#L=['rohan','nahor','okay','hello']
#L='flow	code	wolf	wars	tas listen	fast	silent'.split()

L=[]
while True:
    i=raw_input()
    if i=='.':break
    L.append(i)


def remove_dup(L):
    new=[]
    for item in L:
        if item not in new:new.append(item)
    return new

from itertools import permutations
new=[]
for ind,word in enumerate(L):
    options=[''.join(x) for x in permutations(word)]
    for word2 in L[:ind]+L[ind+1:]:
        if word2 in options:
            new+=[word,word2]
            break
        
x= remove_dup(new)
for i,e in enumerate(x):
    if (i+1)%2==0:
        print e
    else:print e,
    