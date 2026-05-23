nums = [12,15,7,18,20,21,25]
results=list(filter(lambda x:(x % 3 == 0) != (x % 5 == 0),nums))
print(results)
