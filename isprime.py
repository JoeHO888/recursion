def isprime(n,factor=2):
  if factor == n:
    return True
  if n%factor == 0:
    return False
  factor+=1
  return isprime(n,factor)


print(isprime(101))
