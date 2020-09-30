def shuffle(l1,l2):
 list=[]
 m=min(len(l1),len(l2))
 for i in range (0,m):
  list=list+[l1[i]]
  list=list+[l2[i]]
 if (m==len(l1)):
  list=list+l2[m:]
 else:
  list=list+l1[m:]
 return(list)
