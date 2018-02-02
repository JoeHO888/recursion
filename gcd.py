
def gcd(n,k):
  if k == 0:
    return n
  else:
    return gcd(k,n%k)
    
print(gcd(100,6)) #2
