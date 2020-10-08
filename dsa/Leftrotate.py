def leftrotate(m):
 b=[]
 for i in range (len(m)):
  b.append([])
  for j in range(len(m)):
   b[i].append(m[j][len(m)-i-1])
 return(b)
