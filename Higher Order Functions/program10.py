l=[5,10,15,20,25,30]
from functools import reduce
k=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,list(map(lambda x:x*x,l))))
print(k)