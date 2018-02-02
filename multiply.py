

def multiply(a,b):
  if b == 0:
    return 0
  else:
    return multiply(a,b-1)+a
    
print(multiply(100,7)) #700
