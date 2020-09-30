def fact(f):
  factors=[]
  for i in range (1,f+1):
   if (f%i==0):
    factors=factors+[i]
  return(factors)

def isprime(n):
  k=0
  for i in range (1,n+1):
   if (n%i==0):
    k=k+1
  if (k==2):
   return(1)
  else:
   return(0)

def primeproduct(m):
  if (m>0):
   flist=[]
   flist=fact(m)
   for i in flist:
    j=0
    if (isprime(i)==1):
     j=m//i
     if (isprime(j)==1):
      return(True)
     else:
      return(False)
  else:
   return(False)