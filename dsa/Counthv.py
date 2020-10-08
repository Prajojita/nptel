def counthv(l):
 (hc,vc)=(0,0)
 for i in range (1,len(l)-1):
  if (l[i]>l[i-1]) and (l[i]>l[i+1]):
   hc=hc+1
  elif (l[i]<l[i-1]) and (l[i]<l[i+1]):
   vc=vc+1
 return([hc,vc])
