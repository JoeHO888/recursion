def expoential(base,exp):
  if exp==0:
    return 1
  exp-=1
  return expoential(base,exp)*base
  


print(expoential(10,3)) #1000
