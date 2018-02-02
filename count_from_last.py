
def count_from_last(n):
  if n == 0:
    return 0
  else:
    print(n)
    return count_from_last(n-1)
    
    
print (count_from_last(10))
