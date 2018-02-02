
#input: n=positive integer, k=negative power
def neg_power(n,k):
  if k == 0:
    return 1
  else:
    return neg_power(n,k+1)/n
    
print(neg_power(5,-2)) #0.04
