def delchar(s,c):
 if (len(c)==1):
  s_new=""
  for i in range (0,len(s)):
   if (s[i]!=c[0]):
    s_new=s_new+s[i]
  return(s_new)
 else:
  return(s)