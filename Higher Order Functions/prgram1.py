l=list(map(int(input().split())))
from functools import reduce
k=reduce(lambda x,y:x if x>y else y,l)
print(k)