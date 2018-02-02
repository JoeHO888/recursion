def num(n,player1,player2):
  if n<0:
    return 0
  if n == 0: 
    return 1
  if n>0:
    player1, player2 = player2, player1
    if n%3 == 0:
      return num(n-1,player1,player2)+num(n-2,player1,player2)+num(n-4,player1,player2)
    if n%3 == 1:
      return num(n-1,player1,player2)+num(n-4,player1,player2)
    else:
      return num(n-2, player1,player2)
    
def pickcoin(n,player1,player2):
  if n % 3==0:
    return player2+" "+str(num(n,player1,player2))
  return player1+" "+str(num(n,player1,player2))
    
    
print(pickcoin(30,"ada","bob")) #18272
