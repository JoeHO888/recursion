
def match(s,d):
  if len(s) == 0:
    return True
  else:
    if s[0] in d:
      return match(s[1:],d)
    else:
      return False
    
    
print (match("eat","talent")) #true

