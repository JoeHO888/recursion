def sum_(n):
  if n == 1:
    return 1
  else:
    return sum_(n-1)+n
    
print(sum_(10)) #55
