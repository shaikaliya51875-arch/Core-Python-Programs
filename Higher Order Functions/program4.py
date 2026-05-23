from functools import reduce
nums = [1,2,3,4]
results=reduce(lambda a, b: a + b,nums,10)
print(results)
