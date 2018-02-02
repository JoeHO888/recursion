def reverse(s):
  if " " not in s:
    return s
  last_space=s[::-1].find(" ")

  return s[-last_space:]+" "+reverse(s[:-last_space-1])
  


print(reverse("cat is dog")) #dog is cat
