def fib(n,f0=0,f1=1):
  if n==0:
    return f0
  if n== 1:
    return f1
  return fib(n-2)+fib(n-1)
